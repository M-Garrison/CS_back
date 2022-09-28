from django.db import models

# Create your models here.
class Cache(models.Model):
    name = models.CharField(max_length=40)
    note = models.CharField(max_length=144)
    lat = models.CharField(max_length=40)
    long = models.CharField(max_length=40)