from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, \
    TokenVerifyView
from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path(
        'register/',
        RegisterView.as_view(),
        name='register'),
    path(
        'login/',
        LoginView.as_view(),
        name='login'),
    path(
        'token-auth/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'),
    path(
        'token-refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'),
    path(
        'token-verify/',
        TokenVerifyView.as_view(),
        name='token_verify'),
]
