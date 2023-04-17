from rest_framework.serializers import ModelSerializer

from .models import Comment, Project, Issue


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ["description", "author_user", "issue", "created_time"]


class IssuesSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ["title", "description", "tag", "priority", "status", "created_time"]


class ProjectSerializer(ModelSerializer):
   
    class Meta:
        model = Project
        fields = ["title", "description", "type", "author_user"]
