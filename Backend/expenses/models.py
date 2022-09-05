from django.db import models
from authentication.models import User

# Create your models here.
class Expense(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    category_options = [
        ('ONLINE_SERVICES', 'ONLINE_SERVICES'),
        ('FOOD', 'FOOD'),
        ('TRAVEL', 'TRAVEL'),
        ('RENT', 'RENT'),
        ('OTHERS', 'OTHERS'),
    ]
    category = models.CharField(max_length=20, choices=category_options, default='OTHERS')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE, related_name='expenses')
    date = models.DateField(null=False, blank=False)
    

    def __str__(self):
        return self.owner.username

    class Meta:
        verbose_name_plural = "Expenses"