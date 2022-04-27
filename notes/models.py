from django.db import models
from user.models import *
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Tags(models.Model):
    tag = models.CharField(max_length=256,default="General")

    def __str__(self):
        return self.tag

class Color(models.Model):
    color = models.CharField(max_length=256, default="white")
    
    def __str__(self):
        return self.color



class Note(models.Model):
    title = models.CharField(max_length=256, default="")
    body =  RichTextField(blank=True, null=True)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    created_on = models.DateField()
    author = models.ForeignKey(User,  on_delete=models.CASCADE)

    def __str__(self):
        return self.title

