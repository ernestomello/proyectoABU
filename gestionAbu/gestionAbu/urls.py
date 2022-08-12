# gestionAbu URL Configuration

from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView


urlpatterns = [
    path('', include('socios.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include(('rest_framework.urls')))
]
