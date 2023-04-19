from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Comment, Project, Issue
from .serializers import CommentSerializer, ProjectSerializer, IssuesSerializer


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
       return Comment.objects.all()


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset
    
    def perform_create(self, serializer):
        return serializer.save(author_user=self.request.user)

class IssuesViewset(ModelViewSet):
    serializer_class = IssuesSerializer

    def get_queryset(self):
        return Issue.objects.all()


