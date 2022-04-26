from django.shortcuts import render
from django.views.generic import  CreateView,DeleteView, UpdateView, DetailView
from .models import *
from .forms import *

# Create your views here.
class CreateNotes(CreateView):
    model = Notes
    form_class = NotesCreationForms
    template_name = 'create-notes-page.html'


def displayView(request):
    return render(request, 'display-notes-page.html')


    