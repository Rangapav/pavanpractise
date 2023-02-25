from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def func1(request):
    if x>=18:
        return HttpResponse('<h3><i>YOU ARE ELIGBLE TO VOTE</i></h3>')
    else:
        return HttpResponse('<h3><i>YOU ARE NOT ELIGIBLE TO VOTE</i></h3>')
x=int(input('ENTER ANY NUMBER= '))
