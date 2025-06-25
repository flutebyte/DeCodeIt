from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.CharField(max_length=10)
    language = models.CharField(max_length=25)
    score = models.IntegerField()