from django.contrib import admin

from Bookings.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'date', 'time')
    list_filter = ('product',)
    fieldsets = (
        (None, {'fields': ('user', 'product')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'product')}
         ),
    )


admin.site.register(Book, BookAdmin)
