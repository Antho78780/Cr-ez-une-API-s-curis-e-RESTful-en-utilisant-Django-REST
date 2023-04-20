from django.db import models
from authentification.models import User


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    type = models.CharField(max_length=128)
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)


class Issue(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    tag = models.CharField(max_length=128)
    priority = models.CharField(max_length=128)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=128)
    author_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_time = models.DateTimeField()


class Comment(models.Model):
    description = models.CharField(max_length=1000)
    author_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, null=True)
    created_time = models.DateTimeField()
