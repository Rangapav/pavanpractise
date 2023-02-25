from django.shortcuts import render
from django.http import HttpResponse


def func1(request):
    return HttpResponse('<h1>APP ONE CREATED SUCCESSFULLY</h1>')

# Create your views here.
