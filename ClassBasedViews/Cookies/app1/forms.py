from django import forms

class product(forms.Form):
    pname=forms.CharField()
    pprice=forms.IntegerField()
