#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def hello(request):
    return render(request , 'index1.html')