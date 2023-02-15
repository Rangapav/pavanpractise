from django.shortcuts import render
from app1.models import student

# Create your views here.
def studentdata(request):
    x=student.objects.all()
    z={'y':x}
    return render(request,'template/data.html',z)
