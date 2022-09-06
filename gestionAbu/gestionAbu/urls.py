# gestionAbu URL Configuration

#from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view
#from rest_framework.documentation import include_docs_urls

schema_view = get_swagger_view(title='Proyecto ABU API')

urlpatterns = [
    #path('', include(router.urls)),
    path('',include('socios.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest-framework')),
    path(r'swagger-docs/',schema_view),
    #path(r'docs/', include_docs_urls(title='Proyecto ABU API')),
    path('openapi/', get_schema_view(
            title="Proyecto ABU",
            description="API para varias cosas",
            version="1.0.0"
        ), name='openapi-schema'),
]
