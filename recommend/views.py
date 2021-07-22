from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import CollegeApplication
from django import forms


def welcome(request):
    return render(request, "recommend/welcome.html")


# 简单筛选数据并响应
def welcome_output(request):
    sorter1 = "range_int"
    Range = request.GET.get("input_range")
    str_sciOrLib = request.GET.get("sci_or_lib")
    if str_sciOrLib == "文科":
        sciOrLib = 0
    else:
        sciOrLib = 1
    temp1 = ""
    temp2 = "----------------------------------------------" + "<br>"
    List = CollegeApplication.objects.filter(year_int=2020).filter(range_int__gt=Range).filter(
        sci_or_lib=sciOrLib).order_by(sorter1)[0:20]
    for var in List:
        if var.adv_or_com == 1:
            temp1 += var.school_text + "-" + var.major_text + "-" + str(var.score_int) + "-" + str(var.range_int) \
                     + '-提前批' + "-" + "985:" + str(var.is_985) + "-" + "211:" + str(var.is_211) + "<br>"
        else:
            temp2 += var.school_text + "-" + var.major_text + "-" + str(var.score_int) + "-" + str(var.range_int) \
                     + '-本科批' + "-" + "985:" + str(var.is_985) + "-" + "211:" + str(var.is_211) + "<br>"
    response = temp1 + temp2
    return HttpResponse(response)


class RankForm(forms.Form):
    Rank = forms.IntegerField(label='Your Rank')


def results(request):
    if request.method == 'GET':
        form = RankForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/results/")
        else:
            form = RankForm()
    return render(request, 'welcome.html')


# 返回历年数据
def collegetext(request):
    collegeapplication = CollegeApplication.objects.all()
    return render(request, 'recommend/table.html', {
        'collegeapplication': collegeapplication
    })
