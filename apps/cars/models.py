from django.db import models
from django.utils.translation import gettext_lazy as _


class CarType(models.Model):
    id_car_type = models.IntegerField(
        _("Id")
    )
    name = models.CharField(
        _("Name"),
        max_length=255
    )

class CarMark(models.Model):
    id_car_mark = models.IntegerField(
        _("iId")
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