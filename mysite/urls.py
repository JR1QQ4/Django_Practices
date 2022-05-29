"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from demo import views
from django.urls import re_path

from django.urls import include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('db_compare/', include('db_compare.urls')),
#     path('myapp/', include('myapp.urls'))
# ]

# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     path("", views.index),
#     path("add/", views.add),
#     path("find/", views.find),
#     path("find/<int:sid>", views.find),
#     path("find/<int:sid>/<str:name>", views.find),
#     path('edit/', views.update),
#     re_path(r'^fun/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/$', views.fun),
#     re_path(r'^ask/([0-9]{4})/$', views.ask),
# ]

# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     path('', include('demo.urls')),
# ]

# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     path('', include('demo2.urls')),
# ]

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('demo3.urls')),
]