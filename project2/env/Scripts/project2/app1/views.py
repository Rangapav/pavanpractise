from django.shortcuts import render
from django.http import HttpResponse

def func1(request):
    return HttpResponse('<h1>FIRST PROJECT CREATED SUCCESFULLY</h1>')
# Create your views here.
def func2(request):
    return HttpResponse('<h1>WE WANT TO CREATE SECOND APP ALSO</h1>')
