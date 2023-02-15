from django.db import models
from django.urls import reverse

# Create your models here.
class student(models.Model):
    fname=models.CharField(max_length=60)
    lname=models.CharField(max_length=60)
    location=models.CharField(max_length=60)
    mno=models.IntegerField()

    def get_absolute_url(self):
        return reverse('student',args={self.pk})
