from django.shortcuts import render
import datetime
from django.http import HttpResponse

def Display_current_Time(request):
  s=datetime.datetime.now()
  x=('<h1>DATE AND TIME IS</h1>',s)
  return HttpResponse(x)
# Create your views here.
