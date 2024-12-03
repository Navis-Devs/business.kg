from os.path import basename

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarsPostsViewSet

router = DefaultRouter()
router.register(r'cars-posts', CarsPostsViewSet, basename='cars-posts')

urlpatterns = [
    path('', include(router.urls)),
]
