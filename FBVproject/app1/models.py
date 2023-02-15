from django.db import models

# Create your models here.
class malls(models.Model):
    mallname=models.CharField(max_length=50)
    malllocation=models.CharField(max_length=50)
    mallbudget=models.FloatField()
    openingdate=models.DateField()
    openingguest=models.CharField(max_length=50)
