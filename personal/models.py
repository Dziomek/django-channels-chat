from django.db import models

# Create your models here.

class Message(models.Model):
    content = models.CharField(default='', max_length=50)