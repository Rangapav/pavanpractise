from django.shortcuts import render
from django.http import  HttpResponse
from app1.forms import product
# Create your views here.

def f1(request):
    request.session.set_test_cookie()
    return HttpResponse('<b>Session Start</b>')


def f2(request):
    if request.session.test_cookie_worked():
        print('cookies are enabled')
        request.session.delete_test_cookie()
    return HttpResponse('go to next page')

def Increment(request):
    if 'y' in request.COOKIES:
        y = int(request.COOKIES['y'])+1
    else:
      y = 1
    response = render(request,'template/add.html',{'y':y})
    response.set_cookie('y',y)
    return response

def index(request):
    return render(request,'template/index.html')

def addcookies(request):
    x=product()
    response = render(request,'template/additem.html',{'x':x})
    if request.method =='POST':
            x=product(request.POST)
            if x.is_valid():
                name=x.cleaned_data['pname']
                price=x.cleaned_data['pprice']
                response.set_cookie(name,price,50)
    return response

def display(request):
    return render(request,'template/show.html')
