from atexit import register
from pyexpat import model
from django.http import HttpResponse,HttpResponseForbidden
from django.core import serializers
from django.template.defaultfilters import slugify
from django.apps import apps
#from django.db.models.loading import get_model
#from fileinput import filename
import csv,datetime
from django.contrib import admin
from socios.models import Cuota, Departamento, Descriptor, Persona, Socio, Categoria_socio, MetodoPago, PagoCuota,ActaDescriptor, ActaSocio,Acta,Formacion,LugarTrabajo,PerfilCargo,TipoFormacion

# Register your models here.

admin.site.register(Formacion)
admin.site.register(TipoFormacion)
admin.site.register(PerfilCargo)
admin.site.register(LugarTrabajo)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','apellido_paterno','correo_electronico','celular')
admin.site.register(Persona,PersonaAdmin)

class SocioAdmin(admin.ModelAdmin):
    list_display = ('id_persona','estado','categoria_socio','frecuencia_pago','deuda_socio','contacto')
    list_filter = ('categoria_socio','frecuencia_pago','estado',)
    search_fields = ('id_persona__nombre','id_persona__apellido_paterno',)
   # raw_id_fields = ['categoria_socio']
admin.site.register(Socio,SocioAdmin)

admin.site.register(Categoria_socio)

class CuotaAdmin(admin.ModelAdmin):
    list_display = ('id_socio','estado','anio_mes','fecha_vencimiento',)
    search_fields = ('id_socio__id_persona__nombre','id_socio__id_persona__apellido_paterno',)
    list_filter = ('estado',)
    list_per_page = 30

admin.site.register(Cuota,CuotaAdmin)

admin.site.register(MetodoPago)

class PagoCuotaAdmin(admin.ModelAdmin):
    #list_display = ('id_cuota__id_socio__nombre',)
    pass

admin.site.register(PagoCuota,PagoCuotaAdmin)

class ActaDescriptorInline(admin.TabularInline):
    model = ActaDescriptor
    extra = 0
class ActaSocioInline(admin.TabularInline):
    model =ActaSocio
    extra = 0

class ActaAdmin(admin.ModelAdmin):
    inlines = (ActaDescriptorInline,ActaSocioInline,)
    list_display =('fecha','asunto','contenido',)
    list_filter = ('actadescriptor__descriptor','actasocio__id_socio')
    search_fields = ('contenido',)
    

admin.site.register(Acta,ActaAdmin)
admin.site.register(Descriptor)
admin.site.register(Departamento)

""" def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    opt = modeladmin
    print(modeladmin.model._meta)
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment;' 'filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    #fields = modeladmin.model.objets().filter()
    fields = [field for field in opt.get_fields(request=request)]
    print(fields)
    # Write a first row with header information
    #writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)

    return response 

def export(qs,request, fields=None):
    model = qs.model
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % slugify(model.__name__)
    writer = csv.writer(response)
    # Write headers to CSV file
    if fields:
        headers = fields
    else:
        headers = []
        for field in model._meta.fields:
            headers.append(field.name)
    writer.writerow(headers)
    # Write data to CSV file
    for obj in qs:
        row = []
        for field in headers:
            if field in headers:
                val = getattr(obj, field)
                if callable(val):
                    val = val()
                row.append(val)
        writer.writerow(row)
    # Return CSV file to browser as download
    return response
"""
"""
def admin_list_export(request, model_name, app_label, queryset=None, fields=None, list_display=True):
    """
    #Put the following line in your urls.py BEFORE your admin include
    #(r'^admin/(?P<app_label>[\d\w]+)/(?P<model_name>[\d\w]+)/csv/', 'util.csv_view.admin_list_export'),
"""
    if not request.user.is_staff:
        return HttpResponseForbidden()
    if not queryset:
        model = apps.get_model(app_label, model_name)
        queryset = model.objects.all()
        filters = dict()
        for key, value in request.GET.items():
            if key not in ('ot', 'o'):
                filters[str(key)] = str(value)
        if len(filters):
            queryset = queryset.filter(**filters)
    if not fields:
        if list_display and len(queryset.model._meta.admin.list_display) > 1:
            fields = queryset.model._meta.admin.list_display
        else:
            fields = None
    return export(queryset, fields)

admin_list_export.short_description = 'Export to CSV'  #short description
    #serializers.serialize('csv', queryset, stream=response)
    #return response
"""
def export_as_csv(self, request, queryset):

    meta = self.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response


export_as_csv.short_description = "Exportar Seleccionados"
admin.site.add_action(export_as_csv)