from .models import Note
from django import forms

class NotesCreationForms(forms.ModelForm):
    
    class Meta:
        model = Note
        fields = ("title",'tag','body','created_on','color','author')
        widgets={
            'title' : forms.TextInput(attrs={'class':'form-control py-2'}),
            'body': forms.Textarea(attrs={'class':'form-control py-2'}),
            'tag' : forms.Select(attrs={'class':'form-control py-2'}),
            'color': forms.Select(attrs={'class':'form-control py-2'}),
            'author': forms.TextInput(attrs={'class':'form-control py-2','value':'','id':'elder',"type":"hidden"})
        }