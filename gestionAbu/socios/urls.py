from django.urls import path
from socios import views


#from . import views

urlpatterns = [
    path('socios', views.socio_list),
    path('socios/<int:pk>',views.socio_detail),    
    path('socios/<int:id>/cuotas',views.cuota_detail),
    path('personas',views.persona_list),
    path('personas/<int:pk>',views.persona_detail),
    path('cuotas',views.cuota_list),
    path('cuotas/<int:id>/pagar',views.cuota_pago),
    path('cuotas/socio',views.genera_cuotas), 
    path('metodospago',views.metodo_pago_list),   
]

