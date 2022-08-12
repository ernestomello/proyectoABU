from atexit import register
from django.contrib import admin
from socios.models import Persona, Socio, Categoria_socio

# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','apellido_paterno','correo_electronico','celular')
admin.site.register(Persona,PersonaAdmin)

class SocioAdmin(admin.ModelAdmin):
    list_display = ('id_persona','categoria_socio','frecuencia_pago','fecha_ingreso','fecha_baja',)
    list_filter = ('categoria_socio','frecuencia_pago',)
    search_fields = ('id_persona',)
admin.site.register(Socio,SocioAdmin)

admin.site.register(Categoria_socio)