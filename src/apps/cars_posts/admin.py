from django.contrib import admin
from .models import CarsPosts, Pictures, Region, Towns, Possibility

class PicturesAdmin(admin.TabularInline):
    model = Pictures

@admin.register(CarsPosts)
class CarsPostsAdmin(admin.ModelAdmin):
    inlines = [PicturesAdmin]

    list_display = ('id', 'user', 'generation', 'modification', 'year')
    search_fields = ('user__username', 'mark__name', 'model__name')

class TownsInline(admin.TabularInline):
    model = Towns
    extra = 1

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['region_towns__name', 'name']
    
admin.site.register(Possibility)
