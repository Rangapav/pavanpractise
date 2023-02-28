from django.shortcuts import render
from app1.models import student
from django.views.generic import ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
def Index(request):
    return render(request,'app1/index.html')

def Home(request):
    return render(request,'app1/home.html')

class stdCreateView(CreateView):
    model=student
    success_url = reverse_lazy('pavan')
    fields='__all__'

# def DataCheck(reques):
#     return render(request,'app1/checkdata.html')

def About(request):
    return render(request,'app1/about.html')

def Courses_Offered(request):
    return render(request,'app1/courses.html')

def Achievements(request):
    return render(request,'app1/achievements.html')

def Contactus(request):
    return render(request,'app1/contact.html')
