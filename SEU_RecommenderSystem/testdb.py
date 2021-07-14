# -*- coding: utf-8 -*-

from django.http import HttpResponse
from recommend.models import CollegeApplication


# 数据库操作(设定值可通过前端输入修改)
def testdb(request):
    # 筛选条件
    year = 2020

    # 排序索引
    sorter1 = "range_int"

    # 显示范围
    minIndex = 0
    maxIndex = 20

    temp = ""
    List = CollegeApplication.objects.filter(year_int=year).order_by(sorter1)[minIndex:maxIndex]
    for var in List:
        temp += var.school_text + "-" + var.major_text + "-" + str(var.score_int) + "<br>"
    response = temp
    return HttpResponse(response)
