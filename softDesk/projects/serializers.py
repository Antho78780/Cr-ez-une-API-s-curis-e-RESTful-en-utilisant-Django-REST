from rest_framework.serializers import ModelSerializer

from .models import Comment, Project, Issue


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ["description", "author_user", "issue", "created_time"]
        read_only_fields = ("author_user", "issue",)


class IssuesSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ["title", "description", "tag", "priority", "status", "project", "author_user", "created_time"]
        read_only_fields = ("author_user", "project",)


class ProjectSerializer(ModelSerializer):
   
    class Meta:
        model = Project
        fields = ["title", "description", "type", "author_user"]
        read_only_fields = ("author_user",)
