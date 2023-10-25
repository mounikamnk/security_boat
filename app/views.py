from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *

# Create your views here.
class school_list(ListView):
    model=School
    context_object_name='allso'
    #template_name='app\school_list.html'

class SchoolDetail(DetailView):
    model=School
    context_object_name='DOSI'
    #template_name='app\school_detail.html' 


class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class Schooldelete(DeleteView):
    model=School
    context_object_name='DSO'
    success_url=reverse_lazy('school_list')
