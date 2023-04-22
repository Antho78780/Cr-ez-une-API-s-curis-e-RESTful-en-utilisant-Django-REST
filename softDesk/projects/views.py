from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(self.request.GET)
        queryset = Contributor.objects.all()
        return queryset

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
        

    
    