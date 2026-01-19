from django.db import models

# Create your models here.
class AdoptableManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(is_adopted = False)
        )

class Animal(models.Model):
    img = models.ImageField(upload_to='img/', blank=True, null=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=100)
    is_adopted = models.BooleanField(default=False)
    desc = models.CharField(max_length=250)
    object = models.Manager()
    adoptable = AdoptableManager()
    class Meta:
        ordering = ['age']
        indexes = [
            models.Index(fields=['age'])
        ]

    def __str__(self):
        return self.name

