from os.path import basename

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarsPostsViewSet, CarsPostsDestroyAPIView

router = DefaultRouter()
router.register(r'cars-posts', CarsPostsViewSet, basename='cars-posts')

urlpatterns = [
    path('', include(router.urls)),
    path('delete/<str:id>', CarsPostsDestroyAPIView.as_view()),
]
