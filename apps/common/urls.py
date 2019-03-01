from django.urls import path
from . import views
# from django.conf.urls import static
from django.conf.urls.static import static
import os
from apps.profil.views import go_to_profil
from apps.main.views import main

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    path('user/<int:id_user>', go_to_profil, name="get_profil_user"),
    path('update_profil', views.update_profil, name="update_profil"),

    # ------------------- request contact -------------------
    path('manage_contact', views.manage_contact, name="manage_contact"),
    path('accept_or_decline', views.accept_or_decline, name="accept_or_decline"),
    path('remove_contact', views.remove_contact, name="remove_contact"),

    # ------------------- search users -------------------
    path('get_users_list_search', views.get_users_list_search, name="get_users_list_search"),
    path('search_specific/<category>/<what>', views.search_specific, name="search_specific"),

    # ------------------- Notification -------------------
    path('get_number_new_message', views.get_number_new_message, name="get_number_new_message"),
    path('get_number_new_request_contact', views.get_number_new_request_contact, name="get_number_new_request_contact"),
    path('update_new_notifications', views.update_new_notifications, name="update_new_notifications"),
    path('get_number_new_notifications', views.get_number_new_notifications, name="get_number_new_notifications"),

] #+ static('/media/', document_root=os.path.join(BASE_DIR, 'media'))

#+ static(MEDIA_URL, document_root=MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns += static('/static/', document_root='/static/')
#     urlpatterns += static('/media/', document_root='/media/')