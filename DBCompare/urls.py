# 自己创建的路由文件
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index')
]

















