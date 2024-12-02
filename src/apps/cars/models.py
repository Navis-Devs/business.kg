from django.db import models
from django.db.models import SET_NULL
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField
from versatileimagefield.fields import VersatileImageField
import secrets
import string

class PermissionForFront(models.Model):
    key = models.CharField(
        _("Key"),
        max_length=255
    )
    value = models.CharField(
        _("Value"),
        max_length=255
    )

    def save(self, *args, **kwargs):
        alphabet = string.ascii_letters + string.digits
        self.key = ''.join(secrets.choice(alphabet) for _ in range(32))
        self.value = ''.join(secrets.choice(alphabet) for _ in range(32))
        super().save(*args, **kwargs)


###################################################################################################################################################################################################################

class CarColors(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    name = models.CharField(
        _("Название"),
        max_length=300,
        null=True
    )
    color = models.CharField(
        _("Цвет"),
        max_length=300,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Car colors"
        verbose_name_plural = verbose_name


class CarType(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    name = models.CharField(
        _("Name"),
        max_length=255
    )

    def __str__(self):
        return self.name


class CarMark(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    name = models.CharField(
        _("Name"),
        max_length=255
    )
    img = models.ImageField(
        _("Image"),
        null=True,
        upload_to="cars/mark"
    )
    url_image = models.URLField(max_length=1000, null=True, blank=True)
    id_car_type = models.ForeignKey(
        "CarType",
        verbose_name=_("Id car type"),
        on_delete=models.RESTRICT
    )
    name_rus = models.CharField(
        _("Name rus"),
        max_length=255
    )
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    id_car_mark = models.ForeignKey(
        "CarMark",
        verbose_name=_("Id car mark"),
        on_delete=models.RESTRICT,
        related_name='car_models',
        null=True,
        blank=True
    )
    name = models.CharField(
        _("Name"),
        max_length=255
    )
    id_car_type = models.ForeignKey(
        "CarType",
        verbose_name=_("Id car type"),
        on_delete=models.RESTRICT,
        null=True,
        blank=True
    )
    name_rus = models.CharField(
        _("Name rus"),
        null=True,
        max_length=255
    )
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CarGeneration(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    name = models.CharField(
        _("Name"),
        max_length=255
    )
    id_car_model = models.ForeignKey(
        "CarModel",
        verbose_name=_("Id car model"),
        on_delete=models.RESTRICT,
        related_name='car_generations'
    )
    year_begin = models.CharField(
        _("Year begin"),
        null=True,
        max_length=255
    )
    year_end = models.CharField(
        _("Year end"),
        null=True,
        max_length=255
    )
    id_car_type = models.ForeignKey(
        "CarType",
        verbose_name=_("Id car type"),
        on_delete=SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class CarSerie(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    id_car_model = models.ForeignKey(
        "CarModel",
        verbose_name=_("Id car model"),
        on_delete=SET_NULL,
        null=True,
        blank=True,
    )
    name = models.CharField(
        _("Name"),
        max_length=255
    )
    id_car_generation = models.ForeignKey(
        "CarGeneration",
        verbose_name=_("Id car generation"),
        on_delete=models.RESTRICT,
        related_name = "car_serie"
    )
    id_car_type = models.ForeignKey(
        "CarType",
        verbose_name=_("Id car type"),
        on_delete=SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class CarModification(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    id_car_serie = models.ForeignKey(
        "CarSerie",
        verbose_name=_("Id car serie"),
        on_delete=models.RESTRICT
    )
    id_car_model = models.ForeignKey(
        "CarModel",
        verbose_name=_("Id car model"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    name = models.CharField(
        _("Name"),
        max_length=255
    )
    id_car_type = models.ForeignKey(
        "CarType",
        verbose_name=_("Id car type"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

# Branch 1, From CarModification to CarCharacteristicValue

class CarCharacteristic(models.Model):
    id = models.IntegerField(
        primary_key=True,
    )
    name = models.CharField(
        _("Name"),
        max_length=255
    )
    id_parent = models.ForeignKey(
        "self",
        verbose_name=_("Id parent"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    id_car_type = models.ForeignKey(
        "CarType",
        verbose_name=_("Id car type"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class CarCharacteristicValue(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    value = models.CharField(
        _("Value"),
        max_length=255
    )
    unit = models.CharField(
        _("Unit"),
        max_length=255,
        null=True,
        blank=True
    )
    id_car_characteristic = models.ForeignKey(
        "CarCharacteristic",
        verbose_name=_("Id car characteristic"),
        on_delete=models.RESTRICT,
        null=True,
        related_name="id_car_characteristic_value"
    )
    id_car_modification = models.ForeignKey(
        "CarModification",
        verbose_name=_("Car modification"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    id_car_type = models.ForeignKey(
        "CarType",
        verbose_name=_("Id car type"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    def __str__(self):
        return self.value

# branch 2, from CarModification to CarEquipment

class CarEquipment(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    name = models.CharField(
        _("Name"),
        max_length=255
    )
    id_car_modification = models.ForeignKey(
        "CarModification",
        verbose_name=_("Id car modification"),
        on_delete=models.RESTRICT
    )
    price_min = models.IntegerField(
        _("Price min"),
        null=True,
        blank=True
    )
    id_car_type = models.ForeignKey(
        "CarType",
        verbose_name=_("Id car type"),
        on_delete=SET_NULL,
        null=True,
        blank=True
    )
    year = models.IntegerField(
        _("year"),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class CarOption(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    name = models.CharField(
        _("Name"),
        max_length=255
    )
    id_parent = models.ForeignKey(
        "self",
        verbose_name=_("Id parent"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    id_car_type = models.ForeignKey(
        "CarType",
        verbose_name=_("Id car type"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

class CarOptionValue(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    is_base = models.PositiveSmallIntegerField(
        _("Is base")
    )
    id_car_option = models.ForeignKey(
        "CarOption",
        verbose_name=_("Id car option"),
        on_delete=models.RESTRICT
    )
    id_car_equipment = models.ForeignKey(
        "CarEquipment",
        verbose_name=_("Id car equipment"),
        on_delete=models.RESTRICT
    )
    id_car_type = models.ForeignKey(
        "CarType",
        verbose_name=_("Id car type"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )


class CarGenerationImages(models.Model):
    generation_id = models.ForeignKey(
        CarGeneration,
        on_delete=models.CASCADE,
    )
    img = models.URLField(max_length=1000)
    


class FilterData(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Фильтрация'