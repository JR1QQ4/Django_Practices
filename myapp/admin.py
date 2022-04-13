import imp
from django.contrib import admin

# Register your models here.
from myapp.models import UserInfo


admin.site.register(UserInfo)
