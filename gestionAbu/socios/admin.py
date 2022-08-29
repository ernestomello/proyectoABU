from atexit import register
from django.contrib import admin
from socios.models import Cuota, Descriptor, Persona, Socio, Categoria_socio,Cuota,MetodoPago, PagoCuota,ActaDescriptor, ActaSocio,Acta

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

admin.site.register(MetodoPago)

class PagoCuotaAdmin(admin.ModelAdmin):
    #list_display = ('id_cuota__id_socio__nombre',)
    pass

admin.site.register(PagoCuota,PagoCuotaAdmin)

class ActaDescriptorInline(admin.TabularInline):
    model = ActaDescriptor
    extra = 0
class ActaSocioInline(admin.StackedInline):
    model =ActaSocio
    extra = 0

class ActaAdmin(admin.ModelAdmin):
    inlines = ( ActaDescriptorInline,ActaSocioInline,)
    list_display =('fecha','asunto','contenido',)
    list_filter = ('actadescriptor__descriptor','actasocio__id_socio')
    search_fields = ('contenido',)

admin.site.register(Acta,ActaAdmin)
admin.site.register(Descriptor)

