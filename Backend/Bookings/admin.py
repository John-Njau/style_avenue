from django.contrib import admin

from Bookings.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'product')
    list_filter = ('product',)
    fieldsets = (
        (None, {'fields': ('user', 'category', 'product')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'category', 'product')}
         ),
    )


admin.site.register(Book, BookAdmin)
