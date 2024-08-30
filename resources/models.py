from django.db import models
from django.contrib.auth.models import User

class Paper(models.Model):
    title = models.CharField(max_length=32)
    abstract = models.TextField()
    file = models.FileField(upload_to="files", blank=True)
    image = models.ImageField(upload_to="paper_images")
    Publisher = models.ForeignKey(User, on_delete=models.CASCADE)

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