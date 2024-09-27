from django.urls import path
from .views import CarDataListView, ChoicesView

urlpatterns = [
    path('parameters/', CarDataListView.as_view()),
    path('choice-parameters/', ChoicesView.as_view())
]
