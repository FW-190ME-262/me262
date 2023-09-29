from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


def home(request):
    return HttpResponse('<h1>Глвная<h1/>')


def modeli(request):
    return HttpResponse('<h1>Модели<h1/>')


def contakt(request):
    return HttpResponse('<h1>Кантакты<h1/>')
