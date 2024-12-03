from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class Type(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=100)
    )
    def __str__(self):
        return self.name    
    
    class Meta:
        verbose_name = _("Тип")
        verbose_name_plural = _("Типы")

class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    
    class Meta:
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")
        
class Installment(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Возомжность рассрочек")
        verbose_name_plural = _("Возомжность рассрочки")

class AccountType(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Тип аккаунта")
        verbose_name_plural = _("Типы аккаунтов")

class Floor(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Этаж")
        verbose_name_plural = _("Этажи")

class Serie(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Серия")
        verbose_name_plural = _("Серии")

class Material(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Материал")
        verbose_name_plural = _("Материалы")

class BuildingType(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Здание")
        verbose_name_plural = _("Здания")

class Options(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Опция")
        verbose_name_plural = _("Опции")

class Rooms(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Комната")
        verbose_name_plural = _("Комнаты")

class Condition(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Состояние")
        verbose_name_plural = _("Состояния")

class Document(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=100)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Документ")
        verbose_name_plural = _("Документы")
        
class Possibility(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=100)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Возможность")
        verbose_name_plural = _("Возможности")

class Phone(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Телефон")
        verbose_name_plural = _("Телефоны")

class Internet(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Интернет")
        verbose_name_plural = _("Интернеты")

class Toilet(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Туалет")
        verbose_name_plural = _("Туалеты")

class Canalization(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Канализация")
        verbose_name_plural = _("Канализации")

class Water(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Вода")
        verbose_name_plural = _("Воды")

class Electricity(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Электричество")
        verbose_name_plural = _("Электричества")

class Heating(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Отопление")
        verbose_name_plural = _("Отопления")

class Gas(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Газ")
        verbose_name_plural = _("Газы")

class Balcony(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Балкон")
        verbose_name_plural = _("Балконы")

class Door(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Дверь")
        verbose_name_plural = _("Двери")

class Parking(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Парковка")
        verbose_name_plural = _("Парковки")

class Safety(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Безопасность")
        verbose_name_plural = _("Безопасности")
        
    def __unicode__(self):
        return self.name

class Furniture(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Мебель")
        verbose_name_plural = _("Мебели")

class Flooring(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Напольное покрытие")
        verbose_name_plural = _("Напольные покрытия")

class Exchange(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Обмен")
        verbose_name_plural = _("Обмены")

class RentalTerm(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Срок аренды")
        verbose_name_plural = _("Сроки аренды")

class Irrigation(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Поливная вода")
        verbose_name_plural = _("Поливные воды")

class LandAmenities(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Коммуникация")
        verbose_name_plural = _("Коммуникации")

class LandLocation(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Расположение участка")
        verbose_name_plural = _("Расположения участков")

class LandOptions(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Опция участка")
        verbose_name_plural = _("Опции участков")
        
class BuildingClass(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Класс здания")
        verbose_name_plural = _("Классы зданий")

class BuildingState(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Состояние здания")
        verbose_name_plural = _("Состояния зданий")

class Finishing(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Отделка")
        verbose_name_plural = _("Отделки")

class ParkingType(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Тип парковки")
        verbose_name_plural = _("Типы парковок")

class CommercialType(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Тип коммерческого объекта")
        verbose_name_plural = _("Типы коммерческих объектов")

class RoomLocation(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Расположение комнаты")
        verbose_name_plural = _("Расположения комнат")

class RoomOption(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Опция комнаты")
        verbose_name_plural = _("Опции комнат")
        
class FlatOptions(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Опция дома")
        verbose_name_plural = _("Опции дома")

class Currency(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50),
        sign=models.CharField(max_length=10),
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Валюта")
        verbose_name_plural = _("Валюта")
        
class PriceType(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=10),
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Валюта")
        verbose_name_plural = _("Валюта")
        
class CommentAllowed(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = _("Разрещение комментов")
        verbose_name_plural = _("Разрещение комментов")

# Location


class Region(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField(default=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    zoom = models.IntegerField()
    map = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Town(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField(default=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    zoom = models.IntegerField()
    map = models.CharField(max_length=50)
    region = models.ForeignKey(Region, related_name='towns', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField(default=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    zoom = models.IntegerField()
    town = models.ForeignKey(Town, related_name='districts', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class MicroDistrict(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField(default=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    zoom = models.IntegerField()
    district = models.ForeignKey(District, related_name='micro_districts', on_delete=models.CASCADE)

    def __str__(self):
        return self.name