"""Muscunivers_V2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
import os
from django.conf.global_settings import MEDIA_ROOT, MEDIA_URL

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.authentication.urls')),
    path('', include('apps.chatting.urls')),
    path('', include('apps.main.urls')),
    path('', include('apps.profil.urls')),
    path('', include('apps.common.urls')),
    path('', include('apps.menu.urls')),
    path('', include('apps.publication.urls')),
    path('', include('apps.subject.urls')),
    path('', include('apps.event.urls')),
    # path('', include('apps.authentication.urls')),
] + static('/media/', document_root=os.path.join(BASE_DIR, 'media'))
