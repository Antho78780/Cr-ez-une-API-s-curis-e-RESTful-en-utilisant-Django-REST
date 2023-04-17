from django.contrib import admin
from .models import Comment, Project, Issue
admin.site.register([Comment, Project, Issue])

