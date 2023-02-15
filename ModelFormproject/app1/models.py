from django.db import models

# Create your models here.
class project_k(models.Model):
    projectname=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    assignedto=models.CharField(max_length=50)
    budget=models.IntegerField()
    startdate=models.DateField()
    enddate=models.DateField()
