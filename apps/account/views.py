from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

# 注册
# 登陆
# 注销
# 修改密码  通过邮件修改密码
from apps.main.models import User


# 需要登录验证的接口跳转登录界面的url: 127.0.0.1/xxx/?next=/account/update/
def login_view(request):
    if request.method == "GET":
        next = request.GET.get('next')
        return render(request, 'login.html', {'next': next})
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.POST.get('next')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            next = next if next else '/'
            return redirect(next)
        else:
            return render(request, 'login.html', {'next': next})
    else:
        return render(request, 'login.html')


def register_view(request):
    return render(request, 'register.html')


def logout_view(request):
    logout(request)
    return redirect('/')


# 验证用户是否已经登陆
@login_required()
def update(request):
    user = request.user
    user.save()
    return redirect('/')
