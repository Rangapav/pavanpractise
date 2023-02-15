from django import forms

class facebookLOgin(forms.Form):
    gender=[('sone','SELECT YOUR GENDER'),('MALE','MALE'),('female','FEMALE')]
    LOCATION=[('SYL','SELECT YOUR LOCATION'),('hyd','HYDERABAD'),('viz','VIZAG'),('bng','BANGLORE'),('chen','CHENNAI')]
    firstname=forms.CharField(widget=forms.Textarea)
    mobileno=forms.IntegerField()
    mail=forms.CharField()
    GENDER=forms.CharField(widget=forms.Select(choices=gender))
    LOCATION=forms.CharField(widget=forms.Select(choices=LOCATION))
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
