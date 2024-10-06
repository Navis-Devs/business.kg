from django.urls import include, path
from rest_framework import routers
from apps.main import views

router = routers.SimpleRouter()
router.register(r'', views.CommentView)

urlpatterns = [
    path('', include(router.urls)),
]
