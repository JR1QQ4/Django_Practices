#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.urls import path

from demo3 import views
from demo3.views import MyView

urlpatterns = [
    path('', views.index, name='index'),
    path('resp01', views.resp01, name='resp01'),
    path('resp02', views.resp02, name='resp02'),
    path('resp03', views.resp03, name='resp03'),
    path('resp04', MyView.as_view(), name='resp04'),
    path('resp05', views.resp05, name='resp05'),
    path('resp06', views.resp06, name='resp06'),
    path('resp07', views.resp07, name='resp07'),
]
