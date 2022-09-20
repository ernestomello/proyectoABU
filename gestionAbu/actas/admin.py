from django.contrib import admin
from actas.models import Acta,ActaDescriptor,ActaSocio,Descriptor

# Register your models here.

class ActaDescriptorInline(admin.TabularInline):
    model = ActaDescriptor
    extra = 0

class ActaSocioInline(admin.TabularInline):
    model =ActaSocio
    extra = 0
    can_delete = False

    class Media:
        css = {"all": ("css/style.css",)}

class ActaAdmin(admin.ModelAdmin):
    inlines = (ActaDescriptorInline,ActaSocioInline,)
    list_display =('fecha','asunto','contenido',)
    list_filter = ('actadescriptor__descriptor','actasocio__id_socio')
    search_fields = ('contenido',)
    
admin.site.register(Acta,ActaAdmin)
admin.site.register(Descriptor)