from django.shortcuts import render
from app1.models import  project_k
from app1.forms import project_z

# Create your views here.
def index(request):
    return render(request,'template/index.html')


def prlist(request):
    x= project_k.objects.all()
    return render(request,'template/prl.html',{'y':x})


def adlist(request):
    x=project_z()
    if request.method =='POST':
        x=project_z(request.POST)
        if x.is_valid():
            x.save()
            return index(request)
    return render(request,'template/al.html',{'y':x})
