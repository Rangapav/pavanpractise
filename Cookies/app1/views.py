from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.

def f1(request):
    request.session.set_test_cookie()
    return HttpResponse('<b>Session Start</b>')


def f2(request):
    if request.session.test_cookie_worked():
        print('cookies are enabled')
        request.session.delete_test_cookie()
    return HttpResponse('go to next page')
