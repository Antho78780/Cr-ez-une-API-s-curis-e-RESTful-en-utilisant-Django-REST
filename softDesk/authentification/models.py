from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Contributor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    role = models.CharField(max_length=128)
