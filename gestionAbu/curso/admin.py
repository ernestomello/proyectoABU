from django.contrib import admin
from curso.models import Curso,CursoSocio

# Register your models here.
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Curso,CursoAdmin)

class CursoSocioAdmin(admin.ModelAdmin):
    list_display = ('id_socio','id_curso','anio','importe_matricula','pago_inscripcion')
    search_fields = ('id_socio__id_persona__nombre','id_socio__id_persona__apellido_paterno',)
    list_filter = ('id_curso__nombre','anio','pago_inscripcion')
    #fields = ('identificacion',('nombre','genero'),'apellido_paterno','apellido_materno','fecha_nacimiento',('direccion','departamento'),'celular','telefono',('correo_electronico','user'))
    list_per_page = 30

admin.site.register(CursoSocio, CursoSocioAdmin)