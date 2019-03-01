from django.urls import path
from . import views
# from django.conf.urls import static
from django.conf.urls.static import static
import os
from apps.profil.views import go_to_profil
from apps.main.views import main

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = []