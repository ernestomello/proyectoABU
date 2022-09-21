from tabnanny import verbose
from django.contrib import admin
from actas.models import Acta,ActaDescriptor,ActaSocio,Descriptor,ActaPersona
from daterangefilter.filters import  FutureDateRangeFilter

from personas.models import Persona
# Register your models here.

class ActaDescriptorInline(admin.TabularInline):
    model = ActaDescriptor
    extra = 0
    classes = ['collapse']
    class Meta:
        verbose_name = 'Descriptores'

class ActaSocioInline(admin.TabularInline):
    model = ActaSocio
    extra = 0
    classes = ['collapse']
    class Media:
        css = {"all": ("css/style.css",)}
    class Meta:
        verbose_name_plural = 'Socios Presentes en Acta'

class ActaPersonaInLine(admin.TabularInline):
    model = ActaPersona
    extra = 1
    classes = ['collapse']
    
    class Meta:
        verbose_name = 'Otros Participantes'

class ActaAdmin(admin.ModelAdmin):
    
    inlines = [ActaDescriptorInline,ActaSocioInline,ActaPersonaInLine]
    list_display =('fecha','asunto','contenido',)
    list_filter = (('fecha',FutureDateRangeFilter),'actadescriptor__descriptor','actasocio__id_socio')
    search_fields = ('contenido',)
    fields = (('asunto','fecha'),'contenido')
    
admin.site.register(Acta,ActaAdmin)
admin.site.register(Descriptor)