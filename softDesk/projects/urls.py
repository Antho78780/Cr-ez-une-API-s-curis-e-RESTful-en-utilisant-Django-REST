from django.urls import path
from .views import CommentAPIView

app_name = "projects"

urlpatterns = [
    path("comments/",CommentAPIView.as_view(), name="comments")
]