from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import CollegeApplication, CollegeInformation, Collegelast
from collections import Counter
import copy


def welcome(request):
    return render(request, "recommend/welcome.html")


def major_filter(results_list_1, results_list_0, chosen_list):
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
    return result


# 新页面
def new_page(request):
    Range = request.GET.get("input_range")
    Location = request.GET.get("location")
    Title = request.GET.get("title")
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
    if Location and Title and (int(Location) >= 0 or int(Title) >= 0):
        if Title == 0:
            results_list_0 = CollegeApplication.objects.filter(request=0).filter(
                rank_int__gte=int(Range) - 250).order_by('rank_int').filter(location=Location).filter(is_985=1)
            results_list_1 = CollegeApplication.objects.filter(request=1).filter(
                rank_int__gte=int(Range) - 250).order_by('rank_int').filter(location=Location).filter(is_985=1)
        else:
            results_list_0 = CollegeApplication.objects.filter(request=0).filter(
                rank_int__gte=int(Range) - 250).order_by('rank_int').filter(location=Location).filter(is_211=1)
            results_list_1 = CollegeApplication.objects.filter(request=1).filter(
                rank_int__gte=int(Range) - 250).order_by('rank_int').filter(location=Location).filter(is_211=1)
    else:
        results_list_0 = CollegeApplication.objects.filter(request=0).filter(
            rank_int__gte=int(Range) - 250).order_by('rank_int')
        results_list_1 = CollegeApplication.objects.filter(request=1).filter(
            rank_int__gte=int(Range) - 250).order_by('rank_int')
    results_list_1_g = copy.deepcopy(results_list_1)
    results_list_0_g = copy.deepcopy(results_list_0)
    # results_list_0_n = results_list_0.filter(rank_int__gte=int(Range) - 150).filter(rank_int__lt=int(Range) + 150)
    results_list_0_n = results_list_0.filter(rank_int__gte=int(Range) - 150)
    results_list_1_n = results_list_1.filter(rank_int__gte=int(Range) - 150)
    results_list_1_s = results_list_1.filter(rank_int__gte=int(Range) + 150)
    results_list_0_s = results_list_0.filter(rank_int__gte=int(Range) + 150)
    result_gamble = major_filter(results_list_1_g, results_list_0_g, chosen_list)
    result_safe = major_filter(results_list_1_s, results_list_0_s, chosen_list)
    result_normal = major_filter(results_list_1_n, results_list_0_n, chosen_list)
    # result_gamble为'冲'
    result_gamble.sort(key=lambda k: (k.rank_int + float(
        CollegeInformation.objects.filter(school_text=k.school_text).first().rank_var_float) / 1000000))
    # result_normal为'保'
    result_normal.sort(key=lambda k: (k.rank_int + float(
        CollegeInformation.objects.filter(school_text=k.school_text).first().rank_ave_float)))
    # result_safe为'稳'
    result_safe.sort(key=lambda k: (k.rank_int - float(
        CollegeInformation.objects.filter(school_text=k.school_text).first().rank_var_float) / 1000000))
    return render(request, 'recommend/return.html', {  # 由table.html修改为results.html
        'collegeapplication': result_normal, 'safe': result_safe, 'gamble': result_gamble
    })


# 返回新闻
def news(request):
    return render(request, 'recommend/news.html')


# 返回历年数据
def information(request):
    return render(request, 'recommend/table.html', {'collegelast': Collegelast.objects.all()})


def test(request):
    school = request.GET.get("school")
    major = request.GET.get("major")
    rank1 = 0
    rank2 = 0
    rank3 = 0
    rank4 = 0
    for item in Collegelast.objects.all():
        if item.school_text == school and item.major_text == major:
            if item.year_int == 2017:
                rank1 = item.rank_int
            if item.year_int == 2018:
                rank2 = item.rank_int
            if item.year_int == 2019:
                rank3 = item.rank_int
            if item.year_int == 2020:
                rank4 = item.rank_int
    return render(request, 'recommend/test.html',
                  {'rank1': rank1, 'rank2': rank2, 'rank3': rank3, 'rank4': rank4, "school": school, "major": major})





