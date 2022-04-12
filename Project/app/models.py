from tkinter import CASCADE
from django.db import models

# Create your models here.


class User:
    login = models.models.CharField(max_length=256)
    email = models.models.CharField(max_length=256)
    nick_name = models.models.CharField(max_length=256)
    password = models.models.CharField(max_length=256)


class Tag:
    name = models.models.CharField(max_length=256)

class Like:
    pass
class Question:
    title = models.models.CharField(max_length=256)
    text = models.models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=CASCADE)
    tags = models.ManyToManyField(Tag)
