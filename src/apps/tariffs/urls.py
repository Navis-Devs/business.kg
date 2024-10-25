from django.urls import path

from .views import (
    AutoUPView,
    UrgentView,
)

urlpatterns = [
    path("list/auto-up/", AutoUPView.as_view()),
    path("list/urgent/", UrgentView.as_view()),
]