from django.urls import include, path
from rest_framework import routers
from apps.house import views

router = routers.SimpleRouter()
router.register(r'', views.PropertyView)
router.register(r'', views.ComplexView)
router.register(r'', views.CitiesView)

urlpatterns = [
    path('', include(router.urls)),
]
