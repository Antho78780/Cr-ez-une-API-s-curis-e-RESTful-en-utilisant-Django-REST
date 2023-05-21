from rest_framework.viewsets import ModelViewSet
from projects.permissions import IsContributorProjectAuthenticated
from .models import  Project, Issue, Comment
from authentification.models import Contributor
from .serializers import ProjectSerializer, IssuesSerializer, CommentSerializer
from authentification.serializers import ContributorSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsContributorProjectAuthenticated]
    
    def get_queryset(self):
        queryset = Project.objects.filter(author_user=self.request.user)
        return queryset
   
    def perform_create(self, serializer):
        return serializer.save(author_user=self.request.user)
    
    def get_object(self):
        project = get_object_or_404(Project, id=self.kwargs["pk"])
        self.check_object_permissions(self.request, project)
        return project
       
            
class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorSerializer

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        project = get_object_or_404(Project, id=project_id)
        return Contributor.objects.filter(project=project)
    
    def perform_create(self, serializer):
        project_id = self.kwargs["project_id"]
        project = get_object_or_404(Project, id=project_id)
        return serializer.save(user=self.request.user, project=project)
    

class IssueViewSet(ModelViewSet):
    serializer_class = IssuesSerializer
    permission_classes = [IsContributorProjectAuthenticated]
    
    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        project = get_object_or_404(Project, id=project_id)
        issue =  Issue.objects.filter(project=project)
        self.check_object_permissions(self.request, project)
        return issue
    
    def perform_create(self, serializer):
        project_id = self.kwargs["project_id"]
        project = get_object_or_404(Project, id=project_id)
        self.check_object_permissions(self.request, project)
        return serializer.save(project=project, author_user=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsContributorProjectAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        issue_id= self.kwargs["issue_id"]
        project = get_object_or_404(Project, id=project_id)
        issue = Issue.objects.get(id=issue_id, project=project)
        self.check_object_permissions(self.request, project)
        return Comment.objects.filter(issue=issue)

    def perform_create(self, serializer):
        project_id = self.kwargs["project_id"]
        project = get_object_or_404(Project, id=project_id)
        issue = Issue.objects.get(project=project)
        self.check_object_permissions(self.request, project)
        return serializer.save(author_user=self.request.user, issue=issue)
    
    def update(self, request, *args, **kwargs):
        issue_id = self.kwargs["issue_id"]
        comment_id = self.kwargs["pk"]
        issue = get_object_or_404(Issue, id=issue_id)
        comment = get_object_or_404(Comment, id=comment_id, author_user=self.request.user)
        comment.description = self.request.POST["description"]
        comment.issue = issue
        comment.save()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        comment_id = self.kwargs["pk"]
        comment = get_object_or_404(Comment, id=comment_id, author_user=self.request.user)
        comment.delete()
        return comment
    
    def get_object(self):
        comment_id = self.kwargs["pk"]
        project_id = self.kwargs["project_id"]
        project = get_object_or_404(Project, id=project_id)
        comment = get_object_or_404(Comment, id=comment_id)
        self.check_object_permissions(self.request, project)
        return comment