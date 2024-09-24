from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import TokenProxy
from apps.accounts import models

admin.site.unregister(Group)
# admin.site.register(TokenProxy)


@admin.register(models.User)
class UserAdmin(UserAdmin):
    list_display = ('get_avatar', 'username', 'name', 'is_active', 'date_joined')
    ordering = ('-date_joined',)

    search_fields = ('username', 'name',)
    list_display_links = list_display

    readonly_fields = ('username', 'code',)

    fieldsets = (
        (_('Главная'), {'fields': ('username', 'password')}),
        (_('Персональная информация'), {'fields': ('name', 'balance', '_avatar')}),
        (_('Права доступы'), {
            'fields': ('code', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Важные даты'), {'fields': ('last_login', 'date_joined')}),
    )

    def get_avatar(self, obj):
        if obj.avatar:
            return mark_safe(f'<img style="border-radius: 50%;" src="{obj.avatar}" width="50" height="50" />')
        return "No Avatar"

    get_avatar.short_description = 'Avatar'
