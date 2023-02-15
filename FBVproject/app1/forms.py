from django import forms
from app1.models import malls

class getmalls(forms.ModelForm):
    class Meta:
        model=malls
        fields='__all__'
