from django.contrib import admin
from .models import CarsPosts


@admin.register(CarsPosts)
class CarsPostsAdmin(admin.ModelAdmin):

    list_display = ('user', 'car_type', 'mark', 'model', 'year', 'price')
    search_fields = ('user__username', 'mark__name', 'model__name')
