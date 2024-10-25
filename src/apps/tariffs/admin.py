from django.contrib import admin
from .models import (
    AutoUP,
    Urgent,
)

admin.site.register(AutoUP)
admin.site.register(Urgent)