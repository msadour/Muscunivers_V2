from django.urls import path
from . import views
# from django.conf.urls import static
from django.conf.urls.static import static
import os
from apps.profil.views import go_to_profil
from apps.chatting.views import go_to_chat
from apps.authentication.views import log_out
from django.conf.global_settings import MEDIA_ROOT, MEDIA_URL

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    path('go_to_main', views.go_to_main, name="go_to_main"),
    path('go_to_request_contact', views.go_to_request_contact, name="go_to_request_contact"),
    path('search_users', views.search_users, name="search_users"),
    path('chattings', go_to_chat, name="chattings"),
    path('notification', views.go_to_notifications, name="notification"),
    path('profil', go_to_profil, name="profil"),
    path('settings', views.go_to_settings, name="settings"),
    path('logout', log_out, name="logout"),
]