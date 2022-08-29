# gestionAbu URL Configuration

#from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view


urlpatterns = [
    #path('', include(router.urls)),
    path('',include('socios.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest-framework')),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('openapi', get_schema_view(
            title="Proyecto ABU",
            description="API para varias cosas",
            version="1.0.0"
        ), name='openapi-schema'),
]
