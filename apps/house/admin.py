from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from apps.house import models

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Location


@admin.register(models.Location)
class LocationAdmin(MPTTModelAdmin):
    list_display = ('id', 'city', 'parent')
    search_fields = ('city', 'id')


@admin.register(models.ResidentialCategory)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ('id', 'complex_name', 'parent')
    search_fields = ('complex_name', 'id')


class PicteresInline(admin.TabularInline):
    '''Tabular Inline View for Property '''
    model = models.Pictures
    extra = 1


class SecurityInline(admin.TabularInline):
    '''Tabular Inline View for Security'''

    model = models.Security
    extra = 1


@admin.register(models.Property)
class Property(admin.ModelAdmin):
    list_display = ['id', ]
    inlines = [PicteresInline, ]
