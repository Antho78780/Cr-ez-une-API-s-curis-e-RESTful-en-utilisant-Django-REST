from django.shortcuts import HttpResponse
from authentification.models import User
from .serializers import registerSerializer
from rest_framework import generics


class RegisterViews(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = registerSerializer
