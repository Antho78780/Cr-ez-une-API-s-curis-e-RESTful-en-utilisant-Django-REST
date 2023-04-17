from django.urls import path, include
from .views import CommentViewset, ProjectViewset, IssuesViewset
from rest_framework import routers

app_name = "projects"

router = routers.SimpleRouter()
router.register("", ProjectViewset, basename="projects")
router.register('issue/comments', CommentViewset, basename='comments')
router.register("issue", IssuesViewset, basename="issues")

urlpatterns = [
    path('projects/', include(router.urls))
]