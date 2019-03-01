from django.urls import path
from . import views
# from django.conf.urls import static
from django.conf.urls.static import static
import os
from django.conf.global_settings import MEDIA_ROOT, MEDIA_URL

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    path('get_number_new_message', views.get_number_new_message, name="get_number_new_message"),
    path('chattings', views.go_to_chat, name="chattings"),
    path('chattings/<contact>', views.go_to_chat, name="chattings"),
    path('send_message', views.send_message, name="send_message"),
    path('search_user_chatting', views.see_conversations_by_search, name="search_user_chatting"),
    path('go_to_chat_by_search_form', views.go_to_chat_by_search_form, name="go_to_chat_by_search_form"),
    path('update_conversation', views.update_conversation, name="update_conversation"),
] #+ static('/media/', document_root=os.path.join(BASE_DIR, 'media'))

#+ static(MEDIA_URL, document_root=MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns += static('/static/', document_root='/static/')
#     urlpatterns += static('/media/', document_root='/media/')