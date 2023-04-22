from django.urls import path, include
from .views import ProjectViewset, ContributorViewSet
from rest_framework import routers

app_name = "projects"

router = routers.DefaultRouter()
router.register(r"projects", ProjectViewset, basename="projects")
router.register(r"projects/1/users", ContributorViewSet, basename="contributors")


urlpatterns = router.urls  