from django.contrib import admin
from django.urls import path,include

admin.site.site_header = 'Administración ABU'
admin.site.index_title = 'Panel de control de ABU'
admin.site.site_title = 'Administración ABU'

urlpatterns = [
    path('', include('socios.urls')),
    path('admin/', admin.site.urls)
]

handler404 = 'socios.views.handler404'
