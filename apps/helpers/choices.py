from django.db import models
from django.utils.translation import gettext_lazy as _

class Currency(models.TextChoices):
    USD = 'USD', _("Доллар")
    SOM = 'SOM', _("СОМ")
