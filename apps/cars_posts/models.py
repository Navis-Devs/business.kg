from django.db import models
from apps.accounts.models import BaseModel, User


class CarsPosts(BaseModel):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
