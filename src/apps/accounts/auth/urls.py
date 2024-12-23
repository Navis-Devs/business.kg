from django.urls import path, include
from rest_framework.routers import DefaultRouter


from . import (
    profile,
    register,
    activate_account,
    login,
    check,
    change_password,
    forgot_password,
    logout,
    delete_account
)

router = DefaultRouter()
router.register(r'', profile.ProfileViewSet, basename='profile')
router.register(r'', profile.AccountInfo, basename='user_info')

urls = [
    path('', include(router.urls)),

    path('check/', check.UserCheckView.as_view()),
    path('register/', register.RegisterView.as_view()),
    path('activate/', activate_account.ActivateAccountView.as_view()),
    path('login/', login.LoginView.as_view()),
    path('change-password/', change_password.ChangePasswordView.as_view()),
    path('forgot-password/', forgot_password.ForgotPasswordView.as_view()),
    path('logout/', logout.LogoutAccountView.as_view()),
    path('delete-account/', delete_account.DeleteAccountView.as_view()),
]