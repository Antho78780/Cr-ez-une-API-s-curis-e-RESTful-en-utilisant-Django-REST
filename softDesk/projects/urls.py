from django.urls import path, include
from .views import ProjectViewset
from rest_framework import routers

app_name = "projects"

router = routers.SimpleRouter()
router.register("projects", ProjectViewset, basename="projects")

urlpatterns = [
    path('api/', include(router.urls)),
]