from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import  CreateView,DeleteView, UpdateView, DetailView
from .models import *
from .forms import *


# Create your views here.



def displayView(request):
    notes = Note.objects.filter(author = request.user)
    return render(request, 'display-notes-page.html', {'notes':notes})

class CreateNotes(CreateView):
    model = Note
    form_class = NotesCreationForms
    template_name = 'create-notes-page.html'
    success_url = reverse_lazy(displayView)

class UpdateArticle(UpdateView):
    model = Note
    form_class = NotesUpdateForms
    template_name = 'updateArticle.html'


    