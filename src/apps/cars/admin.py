from django.contrib import admin
from django.utils.safestring import mark_safe
from apps.cars.models import (PermissionForFront, CarColors,
                              CarType, CarMark, CarModel, CarGeneration, CarSerie, CarModification,
                              CarCharacteristic, CarCharacteristicValue, CarEquipment, CarOption, CarOptionValue
                              )


@admin.register(PermissionForFront)
class PermissionForFrontAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if PermissionForFront.objects.count() >= 1:
            return False
        return True


@admin.register(CarColors)
class CarColorsAdmin(admin.ModelAdmin):
    list_display = ["get_color", "name"]

    def get_color(self, obj):
        return mark_safe(f'<div style="width: 20px; height: 20px; border-radius: 50%; background-color: {obj.id};"></div>')

    get_color.short_description = "Car Color"



# @admin.register(CarType)
# class CarTypeAdmin(admin.ModelAdmin):
#     search_fields = ['name']
#

@admin.register(CarMark)
class CarMarkAdmin(admin.ModelAdmin):
    search_fields = ['name', 'name_rus', 'id_car_type__name']


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    search_fields = ['name', 'name_rus', 'id_car_mark__name', 'id_car_type__name']


@admin.register(CarGeneration)
class CarGenerationAdmin(admin.ModelAdmin):
    search_fields = ['name', 'id_car_model__name', 'year_begin', 'year_end', 'id_car_type__name']
#
#
# @admin.register(CarSerie)
# class CarSerieAdmin(admin.ModelAdmin):
#     search_fields = ['name', 'id_car_model__name', 'id_car_generation__name', 'id_car_type__name']
#

@admin.register(CarModification)
class CarModificationAdmin(admin.ModelAdmin):
    search_fields = ['name', 'id_car_serie__name', 'id_car_model__name', 'id_car_type__name']


@admin.register(CarCharacteristic)
class CarCharacteristicAdmin(admin.ModelAdmin):
    search_fields = ['name', 'id_parent__name', 'id_car_type__name',
                     'car_characteristic_value__id_car_modification__name']
    ordering = ['id']


@admin.register(CarCharacteristicValue)
class CarCharacteristicValueAdmin(admin.ModelAdmin):
    search_fields = ['value', 'unit', 'id_car_characteristic__name', 'id_car_modification__name', 'id_car_type__name']


# @admin.register(CarEquipment)
# class CarEquipmentAdmin(admin.ModelAdmin):
#     search_fields = ['name', 'id_car_modification__name', 'id_car_type__name']
#
#
# @admin.register(CarOption)
# class CarOptionAdmin(admin.ModelAdmin):
#     search_fields = ['name', 'id_parent__name', 'id_car_type__name']
#
#
# @admin.register(CarOptionValue)
# class CarOptionValueAdmin(admin.ModelAdmin):
#     search_fields = ['id_car_option__name', 'id_car_equipment__name', 'id_car_type__name']
