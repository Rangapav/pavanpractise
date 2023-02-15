from django import forms
from app1.models import project_k

class project_z(forms.ModelForm):
    class Meta:
        model=project_k
        fields='__all__'
