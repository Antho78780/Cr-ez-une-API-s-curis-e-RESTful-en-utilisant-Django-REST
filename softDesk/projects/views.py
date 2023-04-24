from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import  Project, Issue
from authentification.models import Contributor
from .serializers import ProjectSerializer, IssuesSerializer
from authentification.serializers import ContributorSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Project.objects.filter(author_user=self.request.user)
        return queryset
    
    def perform_create(self, serializer):
        return serializer.save(author_user=self.request.user)
    

class ContributorViewSet(generics.ListCreateAPIView):
    serializer_class = ContributorSerializer
    
    def get_queryset(self):
        return Contributor.objects.all()
    
    
    def get(self, request, *args, **kwargs):
        project_id = self.kwargs["project_id"]
        contributor = Contributor.objects.filter(project=project_id)
        serializer = ContributorSerializer(contributor, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        project_id = self.kwargs["project_id"]
        project = Project.objects.get(id=project_id)
        contributor = Contributor.objects.create(
            user = self.request.user,
            project = project
        )
        queryset = [contributor]
        serializer = ContributorSerializer(queryset, many=True)
        return Response(serializer.data)


class ContributorDestroyViewSet(generics.DestroyAPIView):
    serializer_class = ContributorSerializer

    def get_queryset(self):
        queryset = Contributor.objects.all()
        return queryset
    
    def delete(self, request, *args, **kwargs):
        project_id = self.kwargs["project_id"]
        user_id = self.kwargs["user_id"]
        contributor = Contributor.objects.filter(user=user_id, project=project_id)
        return Response(contributor.delete())


class IssuesViewSet(generics.ListCreateAPIView):
    serializer_class = IssuesSerializer

    def get_queryset(self):
        queryset = Issue.objects.all()
        return queryset
    
    def get(self, request, *args, **kwargs):
        project_id = self.kwargs["project_id"]
        issues = Issue.objects.filter(project=project_id)
        serializer = IssuesSerializer(issues, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        project_id = self.kwargs["project_id"]
        project = Project.objects.get(id=project_id)
        issue = Issue.objects.create(
            project = project,
            author_user = self.request.user
        )
        queryset = [issue]
        serializer = IssuesSerializer(queryset, many=True)
        return Response(serializer.data)


class IssueUpdateDestroyViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=  IssuesSerializer

    def get_queryset(self):
        queryset = Issue.objects.all()
        return queryset
    
    def update(self, request, *args, **kwargs):
        project_id = self.kwargs["project_id"]
        issue_id = self.kwargs["issue_id"]
        issue = Issue.objects.filter(id=issue_id, project=project_id)
        issue.update()
    
    def delete(self, request, *args, **kwargs):
        project_id = self.kwargs["project_id"]
        issue_id = self.kwargs["issue_id"]
        issue = Issue.objects.filter(project=project_id, id=issue_id)
        return Response(issue.delete())
        