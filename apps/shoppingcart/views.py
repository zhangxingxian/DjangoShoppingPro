import datetime
import json
import random
from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core import cache
from django.db.models import F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django_ajax.decorators import ajax
from django_redis import get_redis_connection

from apps.main.models import ShopCar, Order

from django.db import transaction
'''

'''


# 添加到购物车
@ajax
@login_required  # 验证用户是否登陆
def add_car(request):
    result = {'status': 200, 'msg': 'ok'}
    # 获取ajax的get的请求
    if request.method == 'POST':
        try:
            shop_id = request.POST.get('shop_id')
            number = int(request.POST.get('number'))

            # 将数据存到用户数据库
            # 1.此用户购物车数据库有此件商品,则更新数据库此商品的数量
            car = ShopCar.objects.filter(shop_id=shop_id, user_id=request.user.id, status=1)
            updata_number = 0
            if car.exists():
                car.update(number=F('number') + number)
                # 返回data的数据应该是购物车商品种类的数量
                # numberall = ShopCar.objects.all().aggregate(sum('number'))
                result.update(data=updata_number)
                return {'result': result}
            else:
                # 2 此用户购物车数据库没有此商品则加入数据库
                updata_number = 1
                car = ShopCar(number=number, shop_id=shop_id, user_id=request.user.id)
                car.save()
            result.update(data=updata_number)
            print(result)
            return {'result': result}  # https://pypi.org/project/djangoajax/
        except Exception as e:
            result = {'status': 400, 'msg': '添加失败'}
            return {'result': result}
    else:
        result = {'status': 2, 'msg': '不支持的请求方式'}
        return {'result': result}


@login_required
def list(reqeust):
    car_list = ShopCar.objects.filter(user_id=reqeust.user.id)
    for car in car_list:
        car.shop.img = car.shop.image_set \
            .filter(shop=car.shop) \
            .values_list('shop_img_id', flat=True) \
            .first()
    return render(reqeust, 'car.html', {'car_list': car_list})


# 修改购物车商品的数量
def update(reqeust):
    pass


def delete(request):
    pass


@ajax
@login_required
def confirm(request):
    if request.method == 'POST':
        cars_str = request.POST.get('car')
        if cars_str:
            # [{carid:1,number:10}]
            cars = json.loads(cars_str)
            try:
                # 开启事务
                with transaction.atomic():
                    # 生成订单
                    oid = product_order(request, cars)
                    #      做事务相关的操作
                    for car in cars:
                        ShopCar.objects.filter(car_id=car.get('car_id')).update(number=car.get('num'), order_id=oid)
                #    生成订单的操作
                return {'oid': oid}
            except Exception as e:
                transaction.rollback()
        else:
            pass


# 生成订单信息
def product_order(request, cars):
    # 第一步生成订单号  全站必须唯一   尽量大于8位
    user_id = request.user.id
    order_code = f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}{random.randint(100000,999999)}"
    order = Order(order_code=order_code, user_id=user_id)
    order.save()
    return order.oid


@login_required
def confirm1(request):
    oid = request.GET.get('oid')
    shops = ShopCar.objects.filter(order_id=oid)
    return render(request, 'confirm.html', {'shops': shops})