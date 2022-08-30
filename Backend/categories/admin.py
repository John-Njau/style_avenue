from django.contrib import admin
from categories.models import Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'pic', 'description')
    list_filter = ('name',)
    fieldsets = (
        (None, {'fields': ('name', 'pic', 'description')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'pic', 'description')}
         ),
    )


admin.site.register(Category, CategoryAdmin)