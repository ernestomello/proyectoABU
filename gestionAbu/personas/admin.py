from django.contrib import admin
from personas.models import Persona,Departamento,TipoFormacion,Formacion,LugarTrabajo,PerfilCargo

# Register your models here.

admin.site.register(Departamento)
admin.site.register(Formacion)
admin.site.register(TipoFormacion)
admin.site.register(PerfilCargo)
class LugarTrabajoAdmin(admin.ModelAdmin):
    filter_horizontal = ['perfil_cargo']
admin.site.register(LugarTrabajo,LugarTrabajoAdmin)

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
    list_display = ('nombre','apellido_paterno','correo_electronico','celular')
    
admin.site.register(Persona,PersonaAdmin)