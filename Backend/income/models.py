from django.db import models
from authentication.models import User

# Create your models here.
class Income(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    Sources_options = [
        ('SALARY', 'SALARY'),
        ('BUSINESS', 'BUSINESS'),
        ('SIDE-HUSTLES', 'SIDE-HUSTLES'),
        ('ONLINE_WORK', 'RENT'),
        ('OTHERS', 'OTHERS'),
    ]
    source = models.CharField(max_length=20, choices=Sources_options, default='OTHERS')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE, related_name='incomes')
    date = models.DateField(null=False, blank=False)
    

    def __str__(self):
        return str(self.owner) + 's income'

    class Meta:
        verbose_name_plural = "Income"
        ordering = ['-date']

    