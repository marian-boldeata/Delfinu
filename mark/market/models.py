from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
class Product(models.Model):
    nume_produs = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.nume_produs

