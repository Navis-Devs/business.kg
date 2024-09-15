from django.urls import path
from .views import CarDataListView

urlpatterns = [
    path('parameters/', CarDataListView.as_view(), name='car-data-list'),
]
