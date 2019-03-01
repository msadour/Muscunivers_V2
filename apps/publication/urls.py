from django.urls import path
from . import views
import os
from apps.main.views import main

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    path('publication/<publication_id>', main, name="one_publication"),
    path('publish_to_wall', views.publish_to_wall, name="publish_to_wall"),
    path('delete_comment', views.delete_comment, name="delete_comment"),
    path('delete_status', views.delete_status, name="delete_status"),
    path('comment_status', views.comment_status, name="comment_status"),
]