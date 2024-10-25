from django.utils.translation import gettext_lazy as _
from django.db import models
from apps.accounts.models import BaseModel


class AbstractAdFeatures(models.Model):
    # Auto UP related fields
    is_autoup = models.BooleanField(
        _("Is Auto UP"),
        default=False
    )
    autoup_time = models.TimeField(
        _("Auto UP Time"),
        null=True,
        blank=True
    )
    autoup_until = models.DateTimeField(
        _("Auto UP Until"),
        null=True,
        blank=True
    )

    # VIP related fields
    is_vip = models.BooleanField(
        _("Is VIP"),
        default=False
    )
    vipped_until = models.DateTimeField(
        _("Vipped Until"),
        null=True,
        blank=True
    )

    # Premium related fields
    is_premium = models.BooleanField(
        _("Is Premium"),
        default=False
    )
    premium_until = models.DateTimeField(
        _("Premium Until"),
        null=True,
        blank=True
    )
    premium_gradient = models.CharField(
        _("Premium Gradient"),
        max_length=255,
        null=True,
        blank=True
    )
    premium_dark_gradient = models.CharField(
        _("Premium Dark Gradient"),
        max_length=255,
        null=True,
        blank=True
    )

    # Urgent related fields
    is_urgent = models.BooleanField(
        _("Is Urgent"),
        default=False
    )
    urgent_until = models.DateTimeField(
        _("Urgent Until"),
        null=True,
        blank=True
    )

    # Top related fields
    is_top = models.BooleanField(
        _("Is Top"),
        default=False
    )
    topped_until = models.DateTimeField(
        _("Topped Until"),
        null=True,
        blank=True
    )

    # Featured and color related fields
    featured = models.BooleanField(
        _("Featured"),
        null=True,
        blank=True
    )
    ad_color = models.CharField(
        _("Ad Color"),
        max_length=7,  # For hex color codes like #FFFFFF
        null=True,
        blank=True
    )
    ad_dark_color = models.CharField(
        _("Ad Dark Color"),
        max_length=7,
        null=True,
        blank=True
    )
    colored_until = models.DateTimeField(
        _("Colored Until"),
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


DAY_RANGE = [(i, str(i)) for i in range(1, 31)]


class AutoUP(BaseModel):
    days = models.IntegerField(
        _("Days duration"),
        choices=DAY_RANGE,
    )
    price = models.IntegerField(
        _("Price")
    )

    class Meta:
        ordering = ("-days",)
        verbose_name = _("Auto Up")
        verbose_name_plural = _("Auto Up")

    def __str__(self):
        return f"{self.days} - {self.price}сом"
