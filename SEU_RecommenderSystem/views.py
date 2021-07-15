from django.http import HttpResponse
from django.shortcuts import render
import random

def recResuts(request):
    # 测试数据，需要从数据库读取相关数据，以返回推荐结果
    request.encoding = 'utf-8'
    province = request.GET.get("select_province", '')
    category = request.GET.get("select_category", '')
    score = request.GET.get("score", '')
    university_id = str(random.randint(1, 100))
    message = f'测试数据: 你在{province}{category}的省排名为{score}，可以上全国第{university_id}的学校了，恭喜你！'
    return HttpResponse(message)