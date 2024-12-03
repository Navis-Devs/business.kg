from django.contrib import admin
from apps.tariffs import models

@admin.register(models.Colors)
class Colors(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Plans)
class Plans(admin.ModelAdmin):
    list_display = ['id']

@admin.register(models.Tariff)
class Tarrif(admin.ModelAdmin):
    list_display = ['id', 'name', 'amount']
