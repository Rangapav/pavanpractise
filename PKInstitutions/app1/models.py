from django.db import models

# Create your models here.
class student(models.Model):
    firstname=models.CharField(max_length=60)
    lastname=models.CharField(max_length=60)
    gender=[('sel','select your gender'),('m','Male'),('f','Female'),('nan','None Of the above')]
    Gender=models.CharField(choices=gender,max_length=20)
    mobileno=models.CharField(max_length=10)
    email=models.EmailField()
    dateofbirth=models.DateField()
    hq=[('sel','select your highest qualification'),('bsc','Bsc Computers'),('bcom','Bcom'),('be','BE'),('Btech','Btech'),('mca','MCA'),('Pg','PG')]
    HighestQualification=models.CharField(choices=hq,max_length=60)
    py=[('sel','select PassedYear'),('2019','2019'),('2020','2020'),('2021','2021'),('2022','2022'),('2023','2023')]
    PassedYear=models.CharField(choices=py,max_length=10)
    Percentage=models.IntegerField()
    Courses=[('sel','select course'),('aws','AWS'),('data','Data Science'),('ja','Java'),('fend','FrontEnd'),('fullsta','Full Stack Python Developer'),('full','Full Stack Java Developer')]
    Select_course=models.CharField(choices=Courses,max_length=40)
    location=models.CharField(max_length=150)
