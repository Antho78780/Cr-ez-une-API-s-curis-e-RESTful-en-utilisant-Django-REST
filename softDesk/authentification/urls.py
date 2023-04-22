from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers

from authentification.views import RegisterViews
from authentification import views

app_name = "authentification"

urlpatterns = [
    path("token/refresh/auth/", TokenRefreshView.as_view(), name="token_refresh"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("signup/", RegisterViews.as_view(), name="signup"),
]