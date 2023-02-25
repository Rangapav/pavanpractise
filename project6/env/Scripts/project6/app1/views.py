from django.shortcuts import render

# Create your views here.
def f1(request):
    x={'name':'pavan'}
    return render(request,"template/cat.html",x)
def f2(request):
    data={'name':'pavan','age':20,'location':'bng'}
    return render(request,"template/data.html",data)
