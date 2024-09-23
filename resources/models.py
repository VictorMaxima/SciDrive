from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import datetime

class Paper(models.Model):
    title = models.CharField(max_length=32, default="")
    abstract = models.TextField()
    file = models.FileField(upload_to="files", blank=True)
    picture = models.ImageField(upload_to="paper_images")
    Publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(default=datetime.datetime.now())
    eISSN = models.CharField(max_length=32, default="")
    slug = models.SlugField(blank=True, default="")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Paper_Outside(models.Model):
    link = models.TextField(blank=False)
    abstract = models.TextField(blank=False)
    thumbnail = models.ImageField()
class SearchResult(models.Model):
    title = models.CharField(max_length=140)
    link = models.CharField(max_length=140)
    snippet = models.TextField()

class Keyword(models.Model):
    title = models.CharField(max_length=40)
    results = models.ManyToManyField(SearchResult)

    def __str__(self):
        return self.title