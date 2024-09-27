from random import choice

from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.accounts.models import BaseModel, User
from apps.cars.models import (
    CarType,
    CarMark,
    CarModel,
    CarSerie,
    CarModification, CarColors
)
from apps.helpers import choices


class CarsPosts(BaseModel):
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Пользователь")
    )
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
    year = models.IntegerField(
        _("Год выпуска"),
        null=True
    )
    serie = models.ForeignKey(
        to=CarSerie,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Кузов")
    )
    engine = models.CharField(
        _("Тип топлива"),
        max_length=300,
        null=True,
        choices=choices.FuelType.choices
    )
    drive = models.CharField(
        _("Привод"),
        max_length=300,
        null=True,
        choices=choices.DriveType.choices
    )
    transmission = models.CharField(
        _("Тип КПП"),
        max_length=300,
        null=True,
        choices=choices.TransmissionType.choices
    )
    modification = models.ForeignKey(
        to=CarModification,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Модификация")
    )
    steering_wheel = models.CharField(
        _("Расположения руля"),
        max_length=300,
        null=True,
        choices=choices.SteeringWheelPosition.choices
    )

    ''' Media '''
    video_url = models.URLField(
        _("URL to video")
    )

    ''' Описание и комплектация '''

    color = models.ForeignKey(
        to=CarColors,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Цвет")
    )
    condition = models.CharField(
        _("Состояние"),
        max_length=300,
        null=True,
        choices=choices.CarCondition.choices
    )
    mileage = models.IntegerField(
        _("Пробег"),
        null=True
    )
    mileage_unit = models.CharField(
        _("Ед. измерения расстоянии"),
        max_length=300,
        null=True,
        choices=choices.MileageUnit.choices
    )
    description = models.TextField(
        _("Текст объявления"),
        null=True,
        blank=True
    )

    ''' Additional information '''

    availability = models.CharField(
        _("Наличие"),
        max_length=300,
        null=True,
        choices=choices.AvailabilityStatus.choices
    )
    customs_cleared = models.BooleanField(
        _("Растоможен"),
        default=False
    )
    registration = models.CharField(
        _("Учёт"),
        max_length=300,
        null=True,
        choices=choices.RegistrationCountry.choices
    )
    other = models.CharField(
        _("Прочее"),
        max_length=300,
        null=True,
        choices=choices.VehicleStatus.choices
    )

    ''' License plate and VIN / chassis number '''
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    currency = models.CharField(
        _("Валюта"),
        max_length=300,
        null=True,
        choices=choices.Currency.choices
    )
    exchange_possibility = models.CharField(
        max_length=30,
        choices=choices.ExchangePossibility.choices
    )
    installment = models.BooleanField(
        _("Возможно рассрочка"),
        default=False
    )