from django.shortcuts import render
from django.http import HttpResponse

def f2(request):
    return HttpResponse('<h1>APP TWO CREATED SUCCESFULLY</h1>')

# Create your views here.
