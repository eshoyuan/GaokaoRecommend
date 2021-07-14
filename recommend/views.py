from django.http import HttpResponse


# 增加了一个视图，用作测试
def index(request):
    return HttpResponse("Hello, world. This index is for recommender.")