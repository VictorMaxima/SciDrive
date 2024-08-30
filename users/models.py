from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
import datetime

# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    created_at = models.DateTimeField(default=datetime.datetime.now())

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    text = models.TextField(blank=False)

    