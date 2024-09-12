from django.urls import path, include
from .auth import urls

urlpatterns = [
    path("", include(urls.urls))
]