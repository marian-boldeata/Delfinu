from django.db import models
from django.contrib.auth.models import User
from market.models import Product

class Cart_item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.quantity} x {self.product.nume_produs}'

