from django.shortcuts import render,redirect
from app1.models import ModelForm
from app1.forms import FormData
from django.core.mail import send_mail
from django.urls import reverse_lazy
# Create your views here.
def Form(request):
    if request.method == 'POST':
        form = FormData(request.POST)
        if form.is_valid():
            form.save()
            subject = 'Form Submission Confirmation',
            message = f'Thank you for your submission, {form.cleaned_data["FirstName"]}! Your data has been received.Our team will contact you before 24 Hours\n\n' \
                      f'FirstName: {form.cleaned_data["FirstName"]}\n' \
                       f'LastName: {form.cleaned_data["LastName"]}\n' \
                      f'Email: {form.cleaned_data["Email"]}\n' \
                      f'MobileNo: {form.cleaned_data["MobileNo"]}\n' \
                      f'Gender: {form.cleaned_data["Gender"]}\n' \
                      f'Current_Location: {form.cleaned_data["Current_Location"]}\n' \
                      f'Date_of_Birth:{form.cleaned_data["Date_of_Birth"]}\n'\
                      f'Register_date:{form.cleaned_data["Register_date"]}\n'\
                      f'Message: {form.cleaned_data["Message"]}'
            from_email = 'somadipavan@gmail.com'
            recipient_list = [form.cleaned_data["Email"]]
            send_mail(subject, message, from_email, recipient_list)
            return redirect('Confirmation')
    else:
        form = FormData()

    return render(request, 'template/Form.html', {'form': form})

def confirmation_view(request):
    return render(request, 'template/Confirmation.html')
    success_url=reverse_lazy('form')
