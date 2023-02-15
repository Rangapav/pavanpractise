from django.shortcuts import render,redirect
from app1.models import malls
from app1.forms import getmalls
# Create your views here.

def listmalls(request):
    x=malls.objects.all()
    return render(request,'template/mall.html',{'y':x})

def addlist(request):
    x=getmalls()
    if request.method =='POST':
        x=getmalls(request.POST)
        if x.is_valid():
            x.save()
            return redirect('/')
    return render(request,'template/add.html',{'y':x})

def delmall(request,id):
    x= malls.objects.get(id=id)
    x.delete()
    return redirect('/')

def updmall(request,id):
    x=malls.objects.get(id=id)
    if request.method == "POST":
        form=getmalls(request.POST,instance = x)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'template/upd.html',{'y':x})
