from django.urls import path
from .views import CarDataListView, DataView, CarsDataView

urlpatterns = [
    path('parameters/', CarDataListView.as_view()),
    path('public/data/', DataView.as_view()),
    path('car/source', CarsDataView.as_view())
]
