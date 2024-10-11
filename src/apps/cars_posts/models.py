from random import choice
from versatileimagefield.fields import VersatileImageField

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
    is_active = models.BooleanField(
        _("Активный"),
        default=True
    )
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
    serie = models.CharField(
        _("Кузов"),
        max_length=255,
        null=True
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
        _("URL для видео"),
        null=True
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
    price = models.IntegerField(
        _("Цена")
    )
    currency = models.CharField(
        _("Валюта"),
        max_length=300,
        null=True,
        choices=choices.Currency.choices
    )
    exchange_possibility = models.CharField(
        _("Возможность обмена"),
        max_length=30,
        choices=choices.ExchangePossibility.choices,
        null=True,
    )
    installment = models.BooleanField(
        _("Возможно рассрочка"),
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    likes = models.ManyToManyField(
        to=User,
        verbose_name=_("Понравится"),
        related_name="liked_car",
        blank=True
    )
    ''' OneToOne rel '''

    exterior = models.OneToOneField("Exterior", on_delete=models.CASCADE)
    interior = models.OneToOneField("Interior", on_delete=models.CASCADE)
    media = models.OneToOneField("Media", on_delete=models.CASCADE)
    security = models.OneToOneField("Security", on_delete=models.CASCADE)
    options = models.OneToOneField("GeneralOptions", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Car post")
        verbose_name_plural = _("Cars posts")


class Media(models.Model):
    cd = models.BooleanField(default=False)
    dvd = models.BooleanField(default=False)
    mp3 = models.BooleanField(default=False)
    usb = models.BooleanField(default=False)
    subwoofer = models.BooleanField(default=False)

    def __str__(self):
        return "Media Options"


class Exterior(models.Model):
    body_kit = models.BooleanField(default=False)
    tinting = models.BooleanField(default=False)
    spoiler = models.BooleanField(default=False)
    alloy_wheel_rims = models.BooleanField(default=False)
    sunroof = models.BooleanField(default=False)
    winch = models.BooleanField(default=False)
    roofrack = models.BooleanField(default=False)
    trunk = models.BooleanField(default=False)
    hitch = models.BooleanField(default=False)
    panoramic_roof = models.BooleanField(default=False)

    def __str__(self):
        return "Exterior Options"


class Interior(models.Model):
    velour = models.BooleanField(default=False)
    leather = models.BooleanField(default=False)
    window_blinds = models.BooleanField(default=False)
    alcantara = models.BooleanField(default=False)
    combined = models.BooleanField(default=False)
    wood = models.BooleanField(default=False)

    def __str__(self):
        return "Interior Options"


class Security(models.Model):
    abs = models.BooleanField(default=False)
    traction_control = models.BooleanField(default=False)
    vehicle_stability_control = models.BooleanField(default=False)
    airbags = models.BooleanField(default=False)
    parking_sensors = models.BooleanField(default=False)
    rear_view_camera = models.BooleanField(default=False)

    def __str__(self):
        return "Security Options"


class GeneralOptions(models.Model):
    full_power_pack = models.BooleanField(default=False)
    anti_theft_alarm = models.BooleanField(default=False)
    remote_car_starter = models.BooleanField(default=False)
    air_conditioner = models.BooleanField(default=False)
    climate_control_system = models.BooleanField(default=False)
    auto_gas_system = models.BooleanField(default=False)
    cruise_control = models.BooleanField(default=False)
    light_sensor = models.BooleanField(default=False)
    heated_steering_wheel = models.BooleanField(default=False)
    seat_ventilation = models.BooleanField(default=False)
    laser_headlights = models.BooleanField(default=False)
    front_seat_heating = models.BooleanField(default=False)
    all_seat_heating = models.BooleanField(default=False)
    mirror_heating_system = models.BooleanField(default=False)
    xenon_headlights = models.BooleanField(default=False)
    bi_xenon_headlights = models.BooleanField(default=False)
    headlight_washer = models.BooleanField(default=False)
    air_suspension = models.BooleanField(default=False)
    seat_memory = models.BooleanField(default=False)
    steering_wheel_memory = models.BooleanField(default=False)
    rain_sensor = models.BooleanField(default=False)
    onboard_computer = models.BooleanField(default=False)
    headlight_adjustment_system = models.BooleanField(default=False)
    keyless_access = models.BooleanField(default=False)

    def __str__(self):
        return "General Options"


class Pictures(models.Model):
    cars = models.ForeignKey(CarsPosts, on_delete=models.CASCADE, related_name='cars_pictures')
    pictures = VersatileImageField(
        upload_to='car/user/pictures/list/',
    )

    # pictures = ResizedImageField(
    #     force_format="WEBP",
    #     quality=75,
    #     upload_to='house/user/pictures/list/',
    # )

    class Meta:
        verbose_name = _("Фотография")
        verbose_name_plural = _("Фотографии")
