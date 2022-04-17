import imp
from django.contrib import admin

# Register your models here.
from myapp.models import UserInfo


# admin.site.register(UserInfo)


# Stu模型的管理器（装饰器写法）
@admin.register(UserInfo)
class StuAdmin(admin.ModelAdmin):
    # 设置要显示在列表中的内容
    list_display = ('id', 'username', 'password', 'age', 'email')

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('username', 'password', 'age', 'email')

    # 设置每页显示多少条记录，默认是100条
    list_per_page = 10

    # 设置默认排序字段，负号表示降序排序，-id
    ordering = ('id',)

    # 设置默认可编辑字段
    # list_eaitable = ['name', 'email']

