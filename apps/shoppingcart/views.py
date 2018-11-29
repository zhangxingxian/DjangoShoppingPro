from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render
from django_ajax.decorators import ajax

from apps.main.models import ShopCar

'''

'''


# 添加到购物车
@ajax
@login_required   # 验证用户是否登陆
def add_car(request):
    result = {'status': 200, 'msg': 'ok'}
    # 获取ajax的get的请求
    if request.method == 'GET':
        try:
            shop_id = request.GET.get('shop_id')
            number = request.GET.get('number')

            # 将数据存到用户数据库
            # 1.此用户购物车数据库有此件商品,则更新数据库此商品的数量
            car = ShopCar.objects.filter(shop_id=shop_id, user_id=request.user.id, status=1)
            updata_number = 0
            if car.exists():
                car.update(number=F('number') + number)
            else:
                # 2 此用户购物车数据库没有此商品则加入数据库
                updata_number = 1
                car = ShopCar(number=number, shop_id=shop_id, user_id=request.user.id)
                car.save()
            result.update(data=updata_number)
            return JsonResponse(result)
        except Exception as e:
            result = {'status': 400, 'msg': '添加失败'}
            return JsonResponse(result)
    else:
        result = {'status': 2, 'msg': '不支持的请求方式'}
        return JsonResponse(result)


@login_required
def list(reqeust):
    car_list = ShopCar.objects.filter(user_id=reqeust.user.id)
    return  render(reqeust,'cars.html')


# 修改购物车商品的数量
def update(reqeust):
    pass


def delete(request):
    pass
