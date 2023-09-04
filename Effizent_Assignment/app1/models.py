from django.db import models

# Create your models here.
class ModelForm(models.Model):
    FirstName=models.CharField(max_length=60)
    LastName=models.CharField(max_length=60)
    Email=models.EmailField()
    MobileNo=models.BigIntegerField()
    gender=[('F','Female'),('M','Male'),('O','Others')]
    Gender=models.CharField(choices=gender,max_length=50)
    Current_Location=models.CharField(max_length=80)
    Date_of_Birth=models.DateField(help_text = "<em>YYYY-MM-DD</em>.")
    Message=models.TextField()
    Register_date = models.DateTimeField(help_text="<em>%Y-%m-%d %H:%M</em>")
