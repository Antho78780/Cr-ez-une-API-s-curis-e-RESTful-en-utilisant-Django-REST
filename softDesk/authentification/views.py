from .serializers import registerSerializer
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet


class RegisterViews(generics.CreateAPIView):
    serializer_class = registerSerializer
