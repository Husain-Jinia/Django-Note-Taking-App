from django.db import models
import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Tags(models.Model):
    tag = models.CharField(max_length=256,default="General")


class Notes(models.Model):
    title = models.CharField(max_length=256, default="")
    body =  RichTextField(blank=True, null=True)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    created_on = models.DateField()

    def __str__(self):
        return self.title

