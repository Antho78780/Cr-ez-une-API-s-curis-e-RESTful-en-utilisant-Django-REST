from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import  Project
from authentification.models import Contributor
from .serializers import ProjectSerializer
from authentification.serializers import ContributorSerializer


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Project.objects.filter(author_user=self.request.user)
        return queryset
    
    def perform_create(self, serializer):
        return serializer.save(author_user=self.request.user)
    

class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorSerializer

    def get_queryset(self):
        queryset = Contributor.objects.all()
        return queryset
    
    def perform_create(self, serializer):
        print(serializer)
        return super().perform_create(serializer)