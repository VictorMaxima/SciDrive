from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
import datetime
import pycountry


def get_country_choices():
    return [(country.alpha_2, country.name) for country in pycountry.countries]

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

class Individual(User):
    USERNAME_FIELD = "email"
    backend = 'users.forms.MyBackend'
    nationality = models.CharField(max_length=32, choices=get_country_choices())
    field = models.CharField(max_length=32)
    school = models.CharField(max_length=88)
    degrees = [
        ("Masters", "Masters"),
        ("PhD", "Doctorate"),
        ("Bachelors", "Bachelors"),
        ("Associate", "Associate"),
        ("Trade", "Trade"),
        ("Other", "Other")
    ]
    degree =  models.CharField(max_length=32, choices=degrees)


    