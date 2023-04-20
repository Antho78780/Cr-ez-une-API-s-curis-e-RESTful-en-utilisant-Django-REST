from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers

from authentification.views import RegisterViews

app_name = "authentification"

urlpatterns = [
    path("token/refresh/auth/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/signup/", RegisterViews.as_view(), name="signup"),
    path("auth/login/", TokenObtainPairView.as_view(), name="login"),
]