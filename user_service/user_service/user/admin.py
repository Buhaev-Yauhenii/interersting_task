from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


# Register your models here.
class UserAdmin(BaseUserAdmin):
    """create good view of model"""

    ordering = ['id']
    list_display = ['email', 'name', 'is_staff', 'is_superuser', 'balance', 'categories']
    list_editable = ['is_staff', 'is_superuser', 'balance','categories']
    fieldsets = (
        (_('Main information'),
         {'fields': ('email', 'password', 'balance',)}),
        (_('permission'),
         {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('important dates'),
         {'fields': ('last_login',)}),
        (_('Categories'),
         {'fields': ('categories',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (
            _('add new user'), {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'name',
                    'password1',
                    'password2',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'balance',
                    'categories'                )
            }),
    )


admin.site.register(User, UserAdmin)
