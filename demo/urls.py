#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from . import views
from django.urls import path, re_path


urlpatterns = [
    path("", views.index, name='index'),
    path("add/", views.add, name='add'),
    path("find/", views.find),
    path("find/<int:sid>", views.find),
    path("find/<int:sid>/<str:name>", views.find, name='find3'),
    path('edit/', views.update),
    re_path(r'^fun/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/$', views.fun),
    re_path(r'^ask/([0-9]{4})/$', views.ask)
]