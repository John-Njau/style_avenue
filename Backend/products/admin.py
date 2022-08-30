from django.contrib import admin

from products.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image', 'category')
    list_filter = ('name',)
    fieldsets = (
        (None, {'fields': ('name', 'description', 'price', 'image', 'category')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'description', 'price', 'image', 'category')}
         ),
    )


admin.site.register(Product, ProductAdmin)