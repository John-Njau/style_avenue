from unicodedata import category
from django.db import models

from categories.models import Category


# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(Category,  blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True)

    def __str__(self):
        category_name = self.category.name
        product = self.name
        return f'{category_name} - {product}'

