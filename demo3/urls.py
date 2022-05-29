#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.urls import path

from demo3 import views

urlpatterns = [
    path('', views.index),
]
