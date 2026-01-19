from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=100)
    is_adpoted = models.BooleanField(default=False)
    desc = models.CharField(max_length=250)
