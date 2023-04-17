from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentification import views

app_name = "authentification"

urlpatterns = [
    path("token/refresh/auth/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/signup/", views.signup, name="signup"),
    path("auth/login/", TokenObtainPairView.as_view(), name="login")
]