# Generated by Django 4.2.3 on 2023-09-03 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=60)),
                ('LastName', models.CharField(max_length=60)),
                ('Email', models.EmailField(max_length=254)),
                ('MobileNo', models.BigIntegerField()),
                ('Gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Others')], max_length=50)),
                ('Current_Location', models.CharField(max_length=80)),
                ('Date_of_Birth', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('Message', models.TextField()),
                ('Register_date', models.DateTimeField(db_comment='Date and time when the article was published')),
            ],
        ),
    ]