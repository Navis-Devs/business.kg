from django.urls import path
from apps.tariffs.views import ApplyTariffView, TarrifList

urlpatterns = [
    path('', TarrifList.as_view()),
    path('active', ApplyTariffView.as_view())
]
