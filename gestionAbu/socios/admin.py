from atexit import register
from django.contrib import admin
from socios.models import Cuota, Persona, Socio, Categoria_socio,Cuota

# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','apellido_paterno','correo_electronico','celular')
admin.site.register(Persona,PersonaAdmin)

class SocioAdmin(admin.ModelAdmin):
    list_display = ('id_persona','categoria_socio','frecuencia_pago','fecha_ingreso','fecha_baja',)
    list_filter = ('categoria_socio','frecuencia_pago',)
    search_fields = ('id_persona__nombre','id_persona__apellido_paterno',)
admin.site.register(Socio,SocioAdmin)

admin.site.register(Categoria_socio)

class CuotaAdmin(admin.ModelAdmin):
    list_display = ('id_socio','estado','anio_mes','fecha_vencimiento',)
    search_fields = ('id_socio__id_persona__nombre','id_socio__id_persona__apellido_paterno',)
    list_filter = ('estado',)

admin.site.register(Cuota,CuotaAdmin)
