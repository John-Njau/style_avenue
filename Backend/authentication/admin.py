from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


# Register your models here.
class CustomUserAdmin(UserAdmin):
    ordering = ('email',)

    list_display = ('email', 'is_active',
                    'is_staff', 'is_verified', 'last_login',)
    list_filter = ('is_active', 'is_staff', 'is_verified',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active',
                                    'is_verified', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )


admin.site.register(models.User, CustomUserAdmin)
