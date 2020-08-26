from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from s3direct.fields import S3DirectField

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    description = models.TextField()
    picture = S3DirectField(dest='blog_destination')
    article = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField()
    url = models.SlugField(max_length=200)
    is_visible = models.BooleanField(default=False)

    def __str__(self):
        return self.title