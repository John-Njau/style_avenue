from django.contrib import admin
from orders.models import Order, OrderItem
from products.models import Product


# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "ordered_date")
    list_filter = ("ordered_date",)
    filter_horizontal = ("products",)
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
