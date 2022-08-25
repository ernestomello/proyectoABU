from django.urls import path
from socios import views

#from . import views

urlpatterns = [
    path('socio', views.socio_list),
    path('socio/<int:pk>',views.socio_detail),
    path('persona',views.persona_list),
    path('persona/<int:pk>',views.persona_detail),
]

