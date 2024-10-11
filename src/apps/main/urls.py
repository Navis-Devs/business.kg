from django.urls import include, path
from rest_framework import routers
from apps.main import views


router = routers.SimpleRouter()
router.register(r'', views.CommentView)
router.register(r"like", views.LikeViews, basename='likes')


urlpatterns = [
    path('', include(router.urls)),
]
