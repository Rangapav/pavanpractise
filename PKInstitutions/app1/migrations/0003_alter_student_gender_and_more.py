# Generated by Django 4.1.5 on 2023-02-28 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_student_mobileno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Gender',
            field=models.CharField(choices=[('sel', 'select your gender'), ('m', 'Male'), ('f', 'Female'), ('nan', 'None Of the above')], max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='HighestQualification',
            field=models.CharField(choices=[('sel', 'select your highest qualification'), ('bsc', 'Bsc Computers'), ('bcom', 'Bcom'), ('be', 'BE'), ('Btech', 'Btech'), ('mca', 'MCA'), ('Pg', 'PG')], max_length=60),
        ),
        migrations.AlterField(
            model_name='student',
            name='PassedYear',
            field=models.CharField(choices=[('sel', 'select PassedYear'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023')], max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='Select_course',
            field=models.CharField(choices=[('sel', 'select course'), ('aws', 'AWS'), ('data', 'Data Science'), ('ja', 'Java'), ('fend', 'FrontEnd'), ('fullsta', 'Full Stack Python Developer'), ('full', 'Full Stack Java Developer')], max_length=40),
        ),
        migrations.AlterField(
            model_name='student',
            name='dateofbirth',
            field=models.DateField(verbose_name='%y-%m-%d'),
        ),
    ]