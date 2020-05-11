from django.db import models

# Create your models here.
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    read_time = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created", "-updated"]


class User(models.Model):
    username = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    Description = models.TextField()
    email = models.CharField(max_length=50)
    password =  models.CharField(max_length=255)
    passcode = models.CharField(max_length=255)
    devices = models.IntegerField(default=0)
    organization = models.IntegerField(default=0)

    def __str__(self):
        return self.username

