from random import choice
from versatileimagefield.fields import VersatileImageField

from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.tariffs.models import TariffStrategyFactory
from django.contrib.contenttypes.fields import GenericRelation
from apps.accounts.models import BaseModel, User, Dealer
from apps.cars.models import (
    CarType,
    CarMark,
    CarModel,
    CarModification,
    CarColors,
    CarGeneration,
    CarSerie
)
from apps.tariffs.models import AbstractAdFeatures
from apps.helpers import choices
from apps.main.models import Review

class CarsPosts(BaseModel, AbstractAdFeatures):
    is_active = models.BooleanField(
        _("Активный"),
        default=True
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Пользователь")
    )
    ''' about car '''
    car_type = models.ForeignKey(
        to=CarType,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Тип")
    )
    mark = models.ForeignKey(
        to=CarMark,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Марка")
    )
    model = models.ForeignKey(
        to=CarModel,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Модель")
    )
    generation_id = models.ForeignKey(
        CarGeneration,
        on_delete=models.CASCADE
    )
    generation = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    modification_id = models.ForeignKey(
        to=CarModification,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Марка")
    )
    modification = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    serie_id = models.ForeignKey(
        CarSerie,
        on_delete=models.CASCADE,
    )
    serie = models.CharField(
        _("Кузов"),
        max_length=100,
        blank=True,
        null=True
    )
    
    
    likes = models.ManyToManyField(
        to=User,
        verbose_name=_("Понравится"),
        related_name="liked_car",
        blank=True
    )
    views = models.PositiveIntegerField(null=True, blank=True, default=1)
    comments = GenericRelation('main.Comments', related_query_name='comments')
    reviews = GenericRelation(Review, related_query_name='reviews')
    dealer_id = models.ForeignKey(
        Dealer,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
    ''' Описание и комплектация '''
    mileage_unit = models.CharField(
        _("Ед. измерения расстоянии"),
        max_length=300,
        null=True,
        choices=choices.MileageUnit.choices
    )
    description = models.TextField(
        _("Текст объявления"),
        null=True,
        blank=True,
    )
    video_url = models.URLField(
        _("URL для видео"),
        blank=True,
        null=True
    )    
    year = models.IntegerField(
        _("Год выпуска"),
        null=True
    )
    horse_power = models.IntegerField(
        _('Лошадинных сил'),
        null=True,
    )
    engine_volume = models.SmallIntegerField(
        _('Объем двигателя'),
        blank=True,
        null=True
    )
    mileage = models.IntegerField(
        _("Пробег"),
        blank=True,
        null=True
    )
    color = models.ForeignKey(
        to=CarColors,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Цвет")
    )
    currency = models.ForeignKey(
        "Currency",
        on_delete=models.CASCADE
    )
    exchange = models.ForeignKey(
        "Exchange",
        on_delete=models.CASCADE,
        null=True
    )
    fuel = models.ForeignKey(
        'Fuel',
        on_delete=models.CASCADE,
        null=True
    )
    installment = models.ForeignKey(
        "Possibility",
        on_delete=models.CASCADE,
        null=True,
        related_name='installment'
    )
    customs = models.ForeignKey(
        "Possibility",
        on_delete=models.CASCADE,
        null=True
    )
    transmission = models.ForeignKey(
        'Transmission',
        on_delete=models.CASCADE,
        null=True
    )
    registration_country = models.ForeignKey(
        "RegistrationCountry",
        on_delete=models.CASCADE,
        null=True
    )
    car_condition = models.ForeignKey(
        "Condition",
        on_delete=models.CASCADE,
        null=True,
    )
    gear_box = models.ForeignKey(
        "GearBox",
        on_delete=models.CASCADE,
        null=True
    )
    featured_option = models.ForeignKey(
        'FeaturedOption',
        on_delete=models.CASCADE,
        null=True,
    )
    steering_wheel = models.ForeignKey(
        'SteeringWheel',
        on_delete=models.CASCADE,
        null=True,
    )
    comment_allowed = models.ForeignKey(
        "CommentAllowed",
        on_delete=models.CASCADE 
    )
    region = models.ForeignKey(
        "Region",
        on_delete=models.CASCADE,
    )
    town = models.ForeignKey(
        "Towns",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    ''' ManyToMany rel '''

    configuration = models.ManyToManyField("GeneralOptions", blank=True)
    interior = models.ManyToManyField("Interior", blank=True)
    exterior = models.ManyToManyField('Exterior', blank=True)
    media = models.ManyToManyField('Media', blank=True)
    safety = models.ManyToManyField('Safety', blank=True)
    other_options = models.ManyToManyField('OtherOptions', blank=True)
    
    
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = _("Car post")
        verbose_name_plural = _("Cars posts")
        ordering = ("-created_at",)
    
    def _apply_tariff(self):
        strategy = TariffStrategyFactory.get_strategy(self.product_id.name)
        if strategy:
            strategy.apply(self)

class Pictures(models.Model):
    cars = models.ForeignKey(CarsPosts, on_delete=models.CASCADE, related_name='pictures')
    pictures = VersatileImageField(
        upload_to='car/user/pictures/list/',
        null=True,
        blank=True,
    )
    
    class Meta:
        verbose_name = _("Фотография")
        verbose_name_plural = _("Фотографии")

class CarPrices(models.Model):
    cars = models.ForeignKey(CarsPosts, on_delete=models.CASCADE, related_name='prices')
    price = models.IntegerField(
        _("Цена"), 
    )
    
    class Meta:
        verbose_name = _("Фотография")
        verbose_name_plural = _("Фотографии")


class GeneralOptions(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Exterior(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class CommentAllowed(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Possibility(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Interior(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Media(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Safety(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Exchange(models.Model):
    name = models.CharField(max_length=100)
    sign = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class OtherOptions(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class SteeringWheel(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Currency(models.Model):
    name = models.CharField(max_length=50)
    sign = models.CharField(max_length=10)
    is_default = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class GearBox(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Condition(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Transmission(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Fuel(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
  
class RegistrationCountry(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class FeaturedOption(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name 


class Region(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Towns(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='towns')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name