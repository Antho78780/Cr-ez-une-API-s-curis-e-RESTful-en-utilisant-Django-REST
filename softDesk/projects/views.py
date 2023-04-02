from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comments
from .serializers import CommentSerializer

# Create your views here.
class CommentAPIView(APIView):

    def get(self, *args, **kwargs):
        comments = Comments.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

