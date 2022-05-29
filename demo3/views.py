from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View


def index(request):
    return render(request, "demo3/index.html")


def resp01(request):
    return HttpResponse("一个简单的视图")


def resp02(request):
    return HttpResponseNotFound('<h1>Page not found.</h1>')

    # return HttpResponse(status=403)

    # raise Http404("Poll does not exist.")


def resp03(request):
    # redirect 重定向，reverse 反向解析
    return redirect(reverse('resp01'))

    # 执行 JS
    # return HttpResponse('<script>alert("添加成功");location.href="/resp01"</script>')

    # 加载一个提示信息跳转页面
    # context = {"info": "数据添加成功", "u": "resp01"}
    # return render(request, 'demo3/info.html', context)


# 视图类的定义
class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, Views!")


# Json数据的响应
def resp05(request):
    data = [
        {'id': 1001, 'name': '张三', 'age': 20},
        {'id': 1002, 'name': '李四', 'age': 22},
        {'id': 1003, 'name': '王五', 'age': 23},
    ]
    return JsonResponse({'data': data})


# cookie 的使用
def resp06(request):
    # # 获取当前的 响应对象
    # response = HttpResponse("cookie 的设置")
    # print(request.COOKIES.get('a', None))
    # # 使用响应对象进行 cookie 的设置
    # response.set_cookie('a', 'abc')

    m = request.COOKIES.get('num', None)
    if m:
        m = int(m) + 1
    else:
        m = 1
    response = HttpResponse("Cookie记录的计数器数值 :" + str(m))

    response.set_cookie("num", m)

    return response


# 测试 request 对象
def resp07(request, ):
    print("请求路径：", request.path)
    print("请求方法：", request.method)
    print("请求编码：", request.encoding)
    print('request.GET: ', request.GET)
    print('id: ', request.GET.get('id'))
    print('name: ', request.GET.get('name'))
    print('age: ', request.GET.get('age', 0))
    return HttpResponse("测试request请求对象")




