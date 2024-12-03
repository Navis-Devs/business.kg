from django.db import models
from django.conf import settings
from apps.accounts.models import BaseModel
from apps.tariffs import models as tariffs_models

class Transaction(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    # tariff = models.ForeignKey(
    #     tariffs_models,
    # )