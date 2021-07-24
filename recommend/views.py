from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import CollegeApplication
from .models import CollegeInformation
from collections import Counter
import copy

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


def results(request):
    result = CollegeApplication.objects.all()
    template = loader.get_template('recommend/results.html')
    context = {
        'list': result,
    }
    return HttpResponse(template.render(context, request))


# 新页面
def new_page(request):
    Range = request.GET.get("input_range")
    get_list = [
        request.GET.get('cbox_Phy'),
        request.GET.get('cbox_Che'),
        request.GET.get('cbox_Bio'),
        request.GET.get('cbox_Pol'),
        request.GET.get('cbox_His'),
        request.GET.get('cbox_Geo')
    ]
    chosen_list = []
    for i in get_list:
        if i == '1':
            chosen_list.append(1)
        else:
            chosen_list.append(0)
    results_list_0 = CollegeApplication.objects.filter(request=0).filter(rank_int__gt=Range).order_by('rank_int')
    results_list_1 = CollegeApplication.objects.filter(request=1).filter(rank_int__gt=Range).order_by('rank_int')
    result = []
    for i in results_list_1:
        request_list = [int(i.Phy),
                        int(i.Che),
                        int(i.Bio),
                        int(i.Pol),
                        int(i.His),
                        int(i.Geo),
                        ]
        temp = [chosen_list[i] - request_list[i] for i in range(len(chosen_list))]
        c1 = Counter(request_list)[1]
        c2 = Counter(temp)[-1]
        if c2 <= c1 - 1:
            result.append(i)
    for i in results_list_0:
        request_list = [int(i.Phy),
                        int(i.Che),
                        int(i.Bio),
                        int(i.Pol),
                        int(i.His),
                        int(i.Geo),
                        ]
        temp = [chosen_list[i] - request_list[i] for i in range(len(chosen_list))]
        if -1 not in temp:
            result.append(i)
    result_safe = copy.deepcopy(result)
    result_gamble = copy.deepcopy(result)
    # result_gamble为'冲'
    result_gamble.sort(key=lambda k: (k.rank_int + float(
        CollegeInformation.objects.filter(school_text=k.school_text).first().rank_var_float) / 1000000))
    # result为'保'
    result.sort(key=lambda k: (k.rank_int + 3*float(
        CollegeInformation.objects.filter(school_text=k.school_text).first().rank_ave_float)))
    # result_safe为'稳'
    result_safe.sort(key=lambda k: (k.rank_int - float(
        CollegeInformation.objects.filter(school_text=k.school_text).first().rank_var_float) / 1000000))
    # 之后可以在前端添加，将result_safe和result_gamble也一起输出
    return render(request, 'recommend/return.html', {  # 由table.html修改为results.html
        'collegeapplication': result  # 这里目前只输出'保'的结果
    })
