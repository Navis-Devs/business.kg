from django.urls import path, include
from .auth import urls

from .views import TariffPlanView

urlpatterns = [
    path("", include(urls.urls)),

    path("tariff/list/", TariffPlanView.as_view())
]