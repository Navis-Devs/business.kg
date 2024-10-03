from django.contrib import admin
from .models import CarsPosts, Pictures

class PicturesAdmin(admin.TabularInline):
    model = Pictures

@admin.register(CarsPosts)
class CarsPostsAdmin(admin.ModelAdmin):
    inlines = [PicturesAdmin]

    list_display = ('user', 'car_type', 'mark', 'model', 'year', 'price')
    search_fields = ('user__username', 'mark__name', 'model__name')
