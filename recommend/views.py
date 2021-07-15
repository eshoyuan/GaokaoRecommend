from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import CollegeApplication


def welcome(request):
    return render(request, "recommend/welcome.html")


def results(request):
    results_list = CollegeApplication.objects.filter(year_int=2020).order_by('range_int')[0:19]
    template = loader.get_template('recommend/results.html')
    context = {
        'list': results_list,
    }
    return HttpResponse(template.render(context, request))
