from django.contrib import admin
from .models import (
    AutoUP,
    Urgent,
    Highlight,
)

admin.site.register(AutoUP)
admin.site.register(Urgent)
admin.site.register(Highlight)