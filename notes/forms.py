from .models import Notes
from django import forms

class NotesCreationForms(forms.ModelForm):
    
    class Meta:
        model = Notes
        fields = ("title",'tag','body','created_on')
        widgets={
            'title' : forms.TextInput(attrs={'class':'form-control py-2'}),
            'body': forms.Textarea(attrs={'class':'form-control py-2'}),
            'tag' : forms.Select(attrs={'class':'form-control py-2'}),
        }