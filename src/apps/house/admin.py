from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from apps.house import models
from django_admin_geomap import ModelAdmin as MapAdmin
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from django.utils.safestring import mark_safe


@admin.register(models.Location)
class LocationAdmin(MPTTModelAdmin):
    list_display = ('id', 'city', 'parent')
    search_fields = ('city', 'id')


@admin.register(models.ResidentialCategory)
class CategoryAdmin(MapAdmin):
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"
    geomap_default_longitude = "74.6066926"
    geomap_default_latitude = "42.8777895"
    geomap_default_zoom = "12"
    geomap_height = "500px"
    list_display = ('complex_name', 'object_state', 'get_media')
    search_fields = ('complex_name', 'id')

    def get_media(self, obj):
        if obj.media:
            return mark_safe(f"<img src='{obj.media.url}' height='61' width='80'>")
        return None

    get_media.short_description = 'видимость обьекта'


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
    list_display = ['id', 'active_post']
    inlines = [PicteresInline, ]


@admin.register(models.Security)
class Security(admin.ModelAdmin):
    list_display = ['id', ]