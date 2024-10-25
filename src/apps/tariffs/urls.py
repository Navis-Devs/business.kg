from django.urls import path

from .views import (
    AutoUPView,
)

urlpatterns = [
    path("list/auto-up/", AutoUPView.as_view()),
]