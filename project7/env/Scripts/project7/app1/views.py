from django.shortcuts import render


def student(request):
    myDetails={'student1':'pavan'}
    return render(request,'template/pavan.html',myDetails)




# Create your views here.
