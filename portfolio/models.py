from django.db import models
from ckeditor.fields import RichTextField
from s3direct.fields import S3DirectField

# Create your models here.
class Project(models.Model):
    title = models.TextField()
    picture =  S3DirectField(dest='portfolio_destination')
    description = RichTextField(blank=True, null=True)
    link = models.TextField()
    priority = models.IntegerField()

    def __str__(self):
        return self.title