from django.http import response
from django.shortcuts import render, redirect


def homepage(requect):
    visit_count = requect.COOKIES.get('visit_count', '0')
    visit_count = int('visit_count') + 1
    response = render(requect, 'cookie_html', {'visit_count': visit_count})
    response.set_cookie('visit_count', visit_count)
    return response


def dalete_cookie(request):
    response = redirect('home')
    response.dalete_cookie('visit_count')
    return response
