# gestionAbu URL Configuration

#from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    #path('', include(router.urls)),
    path('',include('socios.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest-framework')),
    
]
