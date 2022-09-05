from django.db import models

from authentication.models import User
from categories.models import Category
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.products

    class Meta:
        verbose_name_plural = "Orders"
        ordering = ['-ordered_date']


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=False, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name
