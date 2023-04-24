from django.urls import path, include
from .views import ProjectViewset, ContributorViewSet, ContributorDestroyViewSet, IssuesViewSet, IssueUpdateDestroyViewSet
from rest_framework import routers

app_name = "projects"

router = routers.DefaultRouter()
router.register(r"projects", ProjectViewset, basename="projects")


urlpatterns = [
    path("projects/<project_id>/users/", ContributorViewSet.as_view(), name="contributor"),
    path("projects/<project_id>/users/<user_id>/", ContributorDestroyViewSet.as_view(), name="destroy_user"),
    path("projects/<project_id>/issues/", IssuesViewSet.as_view(), name="issues"),
    path("projects/<project_id>/issues/<issue_id>/", IssueUpdateDestroyViewSet.as_view(), name="update_destroy_issue")
]
urlpatterns += router.urls  