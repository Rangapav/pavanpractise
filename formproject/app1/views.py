from django.shortcuts import render
from app1 import forms
# Create your views here.

def Login(request):
    x=forms.facebookLOgin()
    if request.method =='POST':
       data=forms.facebookLOgin(request.post)
       if data.is_valid:
           print("form is valid")
           print('FIRSTNAME',data.cleaned_data['firstname'])
           print('MOBILENO',data.cleaned_data['mobileno'])
           print('MAIL',data.cleaned_data['mail'])
    return render(request,'template/log.html',{'y':x})
