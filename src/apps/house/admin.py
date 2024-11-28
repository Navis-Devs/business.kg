from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from apps.house import models
from django_admin_geomap import ModelAdmin as MapAdmin
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from django.utils.safestring import mark_safe
from parler.admin import TranslatableAdmin
from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view
from apps.house import data_models
from django.http import HttpResponseRedirect
from apps.house import tasks

class BuildingImageInline(admin.TabularInline):
    '''Tabular Inline View for Property '''
    model = models.BuildingImage
    extra = 1   
@admin.register(data_models.PriceType)
class Test(TranslatableAdmin):
    list_display = ('id', )

@admin.register(data_models.Possibility)
class Possibility(TranslatableAdmin):
    list_display = ('id', )
    
@admin.register(models.Building)
class BuildingAdmin(MapAdmin):
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"
    geomap_default_longitude = "74.6066926"
 
    inlines = [BuildingImageInline, ]

class PicteresInline(admin.TabularInline):
    '''Tabular Inline View for Property '''
    model = models.Pictures
    extra = 1
    
@admin.register(models.Property)
class Property(ExtraButtonsMixin, admin.ModelAdmin):
    list_display = ['id', 'active_post']
    search_fields = ['user__username', 'complex_id__complex_name__icontains']
    inlines = [PicteresInline,  ]
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj and obj.category:
            if obj.category.id == 1:
                form.base_fields.pop('material', None)
                form.base_fields.pop('rental_term', None)
                form.base_fields.pop('irrigation', None)
                form.base_fields.pop('land_options', None)
                form.base_fields.pop('land_amenities', None)
                form.base_fields.pop('land_location', None)
                form.base_fields.pop('water', None)
                form.base_fields.pop('canalization', None)
                form.base_fields.pop('electricity', None)
                form.base_fields.pop('options', None)
                form.base_fields.pop('room_location', None)
                form.base_fields.pop('flat_options', None)
                form.base_fields.pop('toilet', None)
                form.base_fields.pop('commercial_type', None)
                form.base_fields.pop('parking_type', None)
                
        return form
    
    @button(
        change_form=True,
        html_attrs={
        'style': '''
            background-color: rgb(184,0,16);
            color: white;
            padding: 0.563rem 2.75rem;
            border-radius: 0.25rem;
            border: none;
            font-size: 1rem;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s ease;
        ''',
        'onmouseover': 'this.style.backgroundColor="rgb(19,150,19)"',
        'onmouseout': 'this.style.backgroundColor="rgb(38, 80, 89)"',
        'onmousedown': 'this.style.transform="scale(0.95)"',
        'onmouseup': 'this.style.transform="scale(1)"',
        }
    )
    def Выгрузка_house_kg(self, request):
        tasks.load_data(languages=['kg', 'ru', 'en'])
        tasks.load_location.delay()
        tasks.load_complex.delay()
        tasks.load_properties.delay()
        self.message_user(request, "НАЧАЛО ВЫГРУЗКИ ДАННЫХ......")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))