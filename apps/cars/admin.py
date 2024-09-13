from django.contrib import admin
from apps.cars.models import CarType, CarMark

admin.site.register(CarType)
admin.site.register(CarMark)