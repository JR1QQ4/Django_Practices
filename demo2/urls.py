#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='demo2_index'),
    path('users', views.index_users, name='demo2_index_users'),
    path('users/add', views.add_users, name='demo2_add_users'),
    path('users/insert', views.insert_users, name='demo2_insert_users'),
    path('users/del/<int:uid>', views.del_users, name='demo2_del_users'),
    path('users/edit/<int:uid>', views.edit_users, name='demo2_edit_users'),
    path('users/update', views.update_users, name='demo2_update_users'),
]
