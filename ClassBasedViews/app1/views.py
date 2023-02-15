from django.shortcuts import render
from app1.models import student
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy


# Create your views here.
class stdListView(ListView):
    model=student

class stdDetailView(DetailView):
    model=student

class stdCreateView(CreateView):
    model=student
    fields=('fname','lname','location','mno')
class stdUpdateView(UpdateView):
    model=student
    fields=('fname','lname','location','mno')
class stdDeleteView(DeleteView):
     model=student
     fields=('fname','lname','location','mno')
     success_url = reverse_lazy('student')
