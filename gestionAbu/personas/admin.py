from django.contrib import admin
from personas.models import Genero, Persona,Departamento,TipoFormacion,Formacion,LugarTrabajo,PerfilCargo

# Register your models here.

#admin.site.register(Departamento)
#admin.site.register(Formacion)
#admin.site.register(TipoFormacion)
#admin.site.register(PerfilCargo)

"""
class LugarTrabajoAdmin(admin.ModelAdmin):
    filter_horizontal = ['perfil_cargo']
admin.site.register(LugarTrabajo,LugarTrabajoAdmin)
"""
class FormacionInLine(admin.StackedInline):
    model   = Formacion
    extra   = 0
    classes = ['collapse']
class LugarTrabajoInLine(admin.StackedInline):
    model = LugarTrabajo
    extra = 0
    filter_horizontal = ['perfil_cargo']
    classes = ['collapse']

class PersonaAdmin(admin.ModelAdmin):
    inlines = (LugarTrabajoInLine,FormacionInLine)
    list_display = ('nombre_completo','departamento','correo_electronico','celular')
    search_fields = ('nombre','apellido_paterno','apellido_materno')
    list_filter = ('departamento','formacion__tipo_formacion','lugartrabajo__perfil_cargo')
    fields = ('identificacion',('nombre','genero'),'apellido_paterno','apellido_materno','fecha_nacimiento',('direccion','departamento'),'celular','telefono',('correo_electronico','user'))
    list_per_page = 30
    
admin.site.register(Persona,PersonaAdmin)
admin.site.register(Genero)