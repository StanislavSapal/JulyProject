from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    #print(request)
    return HttpResponse('<h2>Hello world</h2>')


def test(request):
    return HttpResponse('<h1>Тестова сторінка</h1>')

