from django.shortcuts import render
from django.views.generic import  CreateView,DeleteView, UpdateView, DetailView
from models import *

# Create your views here.
class CreateNotes(CreateView):
    model = Notes
    template_name = 'create-notes.html'