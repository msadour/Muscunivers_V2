from django.urls import path
from . import views
# from django.conf.urls import static
from django.conf.urls.static import static
import os
from django.conf.global_settings import MEDIA_ROOT, MEDIA_URL

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    path('', views.authentication, name="authentication"),
    path('inscription', views.inscription, name="inscription"),
    path('logout', views.log_out, name="logout"),
    path('connection', views.connection, name="connection"),
] #+ static('/media/', document_root=os.path.join(BASE_DIR, 'media'))

#+ static(MEDIA_URL, document_root=MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns += static('/static/', document_root='/static/')
#     urlpatterns += static('/media/', document_root='/media/')