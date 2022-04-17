from django.shortcuts import render

from django.http import HttpResponse

from myapp.models import UserInfo

# Create your views here.
def index(request):
    return HttpResponse('My App！')

def abc(request):
    return HttpResponse('abc！')

def info(request):
    lists = UserInfo.objects.all()  # 获取所有信息
    for v in lists:
        print(v)
    print(UserInfo.objects.get(id=6))
    return HttpResponse('userinfo')







