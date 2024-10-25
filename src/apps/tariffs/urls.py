from django.urls import path

from .views import (
    AutoUPView,
    UrgentView,
    HighlightView
)

urlpatterns = [
    path("list/auto-up/", AutoUPView.as_view()),
    path("list/urgent/", UrgentView.as_view()),
    path("list/highlight/", HighlightView.as_view()),
]