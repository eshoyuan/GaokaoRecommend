from django.http import HttpResponse
from django.shortcuts import render
# 增加了一个视图，用作测试


def welcome(request):
    return render(request, "recommend/welcome.html")