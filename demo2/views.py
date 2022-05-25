from django.http import HttpResponse
from django.shortcuts import render

from demo2.models import Users


# Create your views here.
def index(request):
    # 执行 Model 操作

    # 添加操作
    # ob = Users()  # 实例化一个新对象（空对象）
    # ob.name = "777"
    # ob.age = 61
    # ob.phone = '7777777777777'
    # ob.save()  # 新对象就是添加，已存在对象则是修改

    # 删除操作
    # mod = Users.objects  # 获取 users 的 model 对象
    # user = mod.get(id=5)
    # for item in mod.all():
    #     print(item.id, item.name, item.age, item.phone)
    # print(user.name)
    # user.delete()

    # 修改操作
    # ob = Users.objects.get(id=4)
    # ob.name = "陈平安"
    # ob.age = 26
    # ob.save()

    # 查询操作
    mod = Users.objects
    # ulist = mod.all()  # 获取所有
    # ulist = mod.filter(name='张三')  # 获取指定数据
    # ulist = mod.filter(age__gte=20)  # 所有age大于20的
    # ulist = mod.filter(age__gte=20)  # 大于等于
    # ulist = mod.filter(age__lte=20)  # 小于等于
    # ulist = mod.order_by("age")
    # print(ulist.count())
    # for u in ulist:
    #     print(u.id, u.name, u.age, u.phone, u.addtime)

    return HttpResponse('首页 <br/> <a href="/users">用户信息管理</a>')


# 浏览用户信息
def index_users(request):
    try:
        ulist = Users.objects.all()
        context = {"userslist": ulist}
        return render(request, "demo2/users/index.html", context)
    except:
        return HttpResponse("没有找到用户信息！")


# 加载添加用户信息表单
def add_users(request):
    try:
        return render(request, "demo2/users/add.html")
    except:
        return HttpResponse("没有找到用户信息！")


# 执行用户信息添加、
def insert_users(request):
    try:
        ob = Users()
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        print(ob.name)
        ob.save()
        context = {"info": "添加成功！"}
    except:
        context = {"info": "添加失败！"}
    return render(request, "demo2/users/info.html", context)


# 执行用户信息删除
def del_users(request, uid=0):
    try:
        ob = Users.objects.get(id=uid)
        ob.delete()
        context = {"info": "删除成功！"}
    except:
        context = {"info": "删除失败！"}
    return render(request, "demo2/users/info.html", context)


# 加载用户信息修改表单
def edit_users(request, uid=0):
    try:
        ob = Users.objects.get(id=uid)
        context = {'user': ob}
        return render(request, "demo2/users/edit.html", context)
    except:
        context = {"info": "没有找到要修改的数据！"}
        return render(request, "demo2/users/info.html", context)


# 执行用户信息修改
def update_users(request):

    try:
        ob = Users.objects.get(id=request.POST['id'])
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        ob.save()
        context = {"info": "修改成功！"}
    except:
        context = {"info": "修改失败！"}
    return render(request, "demo2/users/info.html", context)

