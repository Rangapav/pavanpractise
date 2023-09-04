from django import forms
from app1.models import ModelForm

class FormData(forms.ModelForm):
    class Meta:
        model=ModelForm
        fields='__all__'
