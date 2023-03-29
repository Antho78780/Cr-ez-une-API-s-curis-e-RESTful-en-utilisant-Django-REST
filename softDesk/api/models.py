from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    pass

class Contributors:
    project_id = models.IntegerField()
    role = models.CharField()


class Projects:
    title = models.CharField()
    description = models.CharField()
    type = models.CharField()

class Issues:
    title = models.CharField()
    description = models.CharField()
    tag = models.CharField()
    priority = models.CharField()
    status = models.CharField()
    author_user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_time = models.DateTimeField()


class Comments:
    description = models.CharField()
    author_user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(Issues, on_delete=models.CASCADE)
    created_time = models.DateTimeField()


