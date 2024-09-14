from django.db import models
from django.utils.translation import gettext_lazy as _


class CarType(models.Model):
    name = models.CharField(
        _("Name"),
        max_length=255
    )

    def __str__(self):
        return self.name


class CarMark(models.Model):
    name = models.CharField(
        _("Name"),
        max_length=255
    )
    id_car_type = models.ForeignKey(
        "CarType",
        verbose_name=_("Id car type"),
        on_delete=models.RESTRICT
    )
    name_rus = models.CharField(
        _("Name rus"),
        max_length=255
    )

    def __str__(self):
        return self.name


class CarModel(models.Model):
    id_car_mark = models.ForeignKey(
        "CarMark",
        verbose_name=_("Id car mark"),
        on_delete=models.RESTRICT
    )
    name = models.CharField(
        _("Name"),
        max_length=255
    )
    id_car_type = models.ForeignKey(
        "CarType",
        verbose_name=_("Id car type"),
        on_delete=models.RESTRICT
    )
    name_rus = models.CharField(
        _("Name rus"),
        max_length=255
    )