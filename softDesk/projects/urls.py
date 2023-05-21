from django.urls import path, include
from projects import views
from rest_framework import routers

app_name = "projects"

router1 = routers.DefaultRouter()
router1.register(r"", views.ProjectViewset, basename="projects")

router2 = routers.DefaultRouter()
router2.register(r"users", views.ContributorViewSet, basename="contributor")

router3 = routers.DefaultRouter()
router3.register(r"issues", views.IssueViewSet, basename="issues")

router4 = routers.DefaultRouter()
router4.register(r"comments",views.CommentViewSet, basename="comments")

urlpatterns = [
    path("projects/", include(router1.urls)),
    path("projects/<project_id>/", include(router2.urls)),
    path("projects/<project_id>/", include(router3.urls)),
    path("projects/<project_id>/issues/<issue_id>/", include(router4.urls))
]

urlpatterns += router2.urls
    