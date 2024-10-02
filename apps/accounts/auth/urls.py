from django.urls import path, include
from rest_framework.routers import DefaultRouter


from . import (
    profile,
    register,
    activate_account,
    login,
    check
)

router = DefaultRouter()
router.register(r'', profile.ProfileViewSet, basename='profile')

urls = [
    path('', include(router.urls)),

    path('check/', check.UserCheckView.as_view()),
    path('register/', register.RegisterView.as_view()),
    path('activate/', activate_account.ActivateAccountView.as_view()),
    path('login/', login.LoginView.as_view()),
]