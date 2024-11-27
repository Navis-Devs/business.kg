from django.urls import include, path
from rest_framework import routers
from apps.house import views

router = routers.SimpleRouter()
router.register(r'ads', views.PropertyView)
router.register(r'', views.ComplexView)

urlpatterns = [
    path('', include(router.urls)),
    path('public/data/', views.DataView.as_view()),
    path('param/', views.PropertyParam.as_view())
]
