from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import  Project
from .serializers import ProjectSerializer


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    

    def get_queryset(self):
        queryset = Project.objects.filter(author_user=self.request.user)
        return queryset
    
    def perform_create(self, serializer):
        return serializer.save(author_user=self.request.user)
    
