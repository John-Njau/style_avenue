from django.contrib import admin

from .models import Income

# Register your models here.
class IncomeAdmin(admin.ModelAdmin):
    list_display = ("source","date", "amount", "description","user" )
    read_only_fields = ("id",)


admin.site.register(Income, IncomeAdmin)
