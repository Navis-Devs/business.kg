from django.urls import path

from .views import (
    TopView,
    AutoUPView,
    UrgentView,
    HighlightView,
    SubscribeToTariffView,
)

urlpatterns = [
    path("list/top/", TopView.as_view()),
    path("list/auto-up/", AutoUPView.as_view()),
    path("list/urgent/", UrgentView.as_view()),
    path("list/highlight/", HighlightView.as_view()),

    # process
    path("activate/", SubscribeToTariffView.as_view()),
]