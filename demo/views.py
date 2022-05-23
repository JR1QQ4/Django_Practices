from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def index(request):
    print(reverse('add'))  # reverse 通过路由名称反向生成 url 请求地址
    print(reverse('index'))
    print(reverse('find3', args=(100, 'zhangsan')))
    return redirect(reverse('find3', args=(100, 'zhangsan')))
    # return HttpResponse('Hello World!')


def add(request):
    return HttpResponseRedirect(reverse('find3', args=(100, 'zhangsan')))
    # return HttpResponse('add...')


# def find(request, sid):
#     return HttpResponse('find...%d' % sid)


def find(request, sid=0, name=""):
    if name == "":
        return HttpResponse('find...%d' % sid)
    else:
        return HttpResponse('find...%d, %s' % (sid, name))


def update(request):
    raise Http404('修改页面不存在！')
    # return HttpResponse('update...')


def ask(request, y):
    return HttpResponse('参数信息：%s 年' % y)


def fun(request, y, m):
    return HttpResponse('参数信息：%s 年 %s 月' % (y, m))

