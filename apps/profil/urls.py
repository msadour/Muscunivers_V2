from django.urls import path
from . import views
# from django.conf.urls import static
from django.conf.urls.static import static
import os
from django.conf.global_settings import MEDIA_ROOT, MEDIA_URL

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    path('profil/<int:id_user>/<window>', views.go_to_profil, name="profil"),
    path('profil', views.go_to_profil, name="profil"),
    path('create_product', views.create_product, name="create_product"),
    path('delete_product', views.delete_product, name="delete_product"),
    path('create_coaching', views.create_coaching, name="create_coaching"),
    path('delete_coaching', views.delete_coaching, name="delete_coaching"),
    path('create_event', views.create_event, name="create_event"),
    path('create_subject', views.create_subject, name="create_subject"),
] #+ static('/media/', document_root=os.path.join(BASE_DIR, 'media'))

#+ static(MEDIA_URL, document_root=MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns += static('/static/', document_root='/static/')
#     urlpatterns += static('/media/', document_root='/media/')