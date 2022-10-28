from unicodedata import name
from django.db import models

# Create your models here.
class Listing(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    milage = models.IntegerField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name
