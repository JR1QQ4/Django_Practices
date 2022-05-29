from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "demo3/index.html")


def resp01(request):
    return HttpResponse("一个简单的视图")