from django.urls import path
from .views import CarDataListView, DataView

urlpatterns = [
    path('parameters/', CarDataListView.as_view()),
    path('public/data/', DataView.as_view())
]
