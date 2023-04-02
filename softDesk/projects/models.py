from django.db import models
from authentification.models import Users


class Projects(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    type = models.CharField(max_length=128)
    author_user = models.ForeignKey(Users, on_delete=models.CASCADE)

class Issues(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    tag = models.CharField(max_length=128)
    priority = models.CharField(max_length=128)
    status = models.CharField(max_length=128)
    created_time = models.DateTimeField()


class Comments(models.Model):
    description = models.CharField(max_length=1000)
    author_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_time = models.DateTimeField()
