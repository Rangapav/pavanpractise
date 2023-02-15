from django.db import models

# Create your models here.
class student(models.Model):
    fname=models.CharField(max_length=40)
    lname=models.CharField(max_length=40)
    age=models.IntegerField()
    location=models.CharField(max_length=40)
    mobileno=models.IntegerField()
