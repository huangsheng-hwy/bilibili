from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def django_demo(request):
    # return HttpResponse("hello")
    return render(request, 'g_推文/huo_鼠标火花.html')


def data_demo(request):
    # return HttpResponse("hello")
    return render(request, 'g_推文/shijie.html')
