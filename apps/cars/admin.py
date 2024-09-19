from django.contrib import admin
from apps.cars.models import (PermissionForFront,
    CarType, CarMark, CarModel, CarGeneration, CarSerie, CarModification,
    CarCharacteristic, CarCharacteristicValue, CarEquipment, CarOption, CarOptionValue
)

class PermissionForFrontAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if PermissionForFront.objects.count() >= 1:
            return False
        return True

admin.site.register(PermissionForFront, PermissionForFrontAdmin)

admin.site.register(CarType)
admin.site.register(CarMark)
admin.site.register(CarModel)
admin.site.register(CarGeneration)
admin.site.register(CarSerie)
admin.site.register(CarModification)
admin.site.register(CarCharacteristic)
admin.site.register(CarCharacteristicValue)
admin.site.register(CarEquipment)
admin.site.register(CarOption)
admin.site.register(CarOptionValue)
