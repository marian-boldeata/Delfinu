from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    nume_produs = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    descriere = models.CharField(max_length=200,default="...")
    pret = models.IntegerField(null=False,default=1)
    cantitate = models.IntegerField(default=1)
    imagine_produs = models.ImageField(upload_to="imagini_produs/", default="mark/no img available")

    def __str__(self):
        return self.nume_produs










