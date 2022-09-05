from django.db import models

from categories.models import Category
from products.models import Product
from authentication.models import User


# Create your models here.
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name_plural = "Booking"

