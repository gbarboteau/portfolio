from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Project(models.Model):
    title = models.TextField()
    picture = models.ImageField(upload_to ='static/uploads/') 
    description = RichTextField(blank=True, null=True)
    link = models.TextField()
    priority = models.IntegerField()

    def __str__(self):
        return self.title