from .serializers import registerSerializer
from rest_framework import generics


class RegisterViews(generics.CreateAPIView):
    serializer_class = registerSerializer
   
   