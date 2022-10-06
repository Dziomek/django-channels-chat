from django.db import models

# Create your models here.


class Message(models.Model):
    room_name = models.CharField(default='', max_length=50)
    username = models.CharField(default='', max_length=50)
    content = models.CharField(default='', max_length=50)


class Room(models.Model):
    room_name = models.CharField(default='', max_length=50)