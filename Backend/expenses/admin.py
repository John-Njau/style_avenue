from django.contrib import admin

from .models import Expense

# Register your models here.
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("category","date", "amount", "description","user" )
    read_only_fields = ("id",)


admin.site.register(Expense, ExpenseAdmin)
