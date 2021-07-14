from django.http import HttpResponse
from django.shortcuts import render
# 增加了一个视图，用作测试
def index(request):
    return HttpResponse("Hello, world. This index is for recommender.")
def welcome(request):
    return render(request, "recommend/welcome.html")