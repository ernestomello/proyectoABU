from datetime import timedelta
from django.contrib import messages, admin
from django.http import HttpResponse
import csv
from socios.models import Cuota, Departamento, Descriptor, Persona, Socio, Categoria_socio, MetodoPago, PagoCuota,ActaDescriptor, ActaSocio,Acta,Formacion,LugarTrabajo,PerfilCargo,TipoFormacion
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import GenerarCuotaForm, RegistroPagoForm

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

class SocioAdmin(admin.ModelAdmin):
    list_display    = ('id_persona','estado','categoria_socio','frecuencia_pago','deuda_socio','contacto')
    list_filter     = ('categoria_socio','frecuencia_pago','estado',)
    search_fields   = ('id_persona__nombre','id_persona__apellido_paterno',)
    change_form_template = "generar-cuota/btn_generar_cuota.html"
    actions         = ['generar_cuota']

    @admin.action(description='Generar Cuota')
    def generar_cuota(self, request, queryset):

        if 'apply' in request.POST:
            print(queryset)
            year_init   = request.POST["fecha_desde_year"]
            year_end    = request.POST["fecha_hasta_year"]
            month_init  = request.POST["fecha_desde_month"]
            month_end   = request.POST["fecha_hasta_month"]
            if Cuota.fecha_inconsistente(year_init, month_init, year_end, month_end):
                self.message_user(request, "Fechas inconsistente, no se generaron cuotas nuevas.", level=messages.ERROR)
            else:
                rango_fechas = Cuota.range_month(year_init, month_init, year_end, month_end)
                cantidad=0
                for socio in queryset:
                    for fecha_valor in rango_fechas:                    
                        cuota = Cuota.objects.get_or_create(
                            id_socio = socio,
                            mes_anio = fecha_valor,
                            fecha_vencimiento = fecha_valor + timedelta(days=10),
                            importe = socio.importe_cuota()
                        )
                        if cuota:
                            cantidad+= 1
                        print(cuota)

                self.message_user(request, "Se generaron {} cuotas".format(cantidad))
            return HttpResponseRedirect(request.get_full_path())

        form = GenerarCuotaForm(initial={'_selected_action': queryset.values_list('id_socio', flat=True)})
        return render(request, "generar-cuota/generar_cuota.html", {'items': queryset, 'form': form})    

admin.site.register(Socio,SocioAdmin)

admin.site.register(Categoria_socio)

class CuotaAdmin(admin.ModelAdmin):
    list_display = ('id_socio','estado','anio_mes','fecha_vencimiento',)
    search_fields = ('id_socio__id_persona__nombre','id_socio__id_persona__apellido_paterno',)
    list_filter = ('estado',)
    list_per_page = 30
    actions = ['registro_pago']

    @admin.action(description='Registrar pago')
    def registro_pago(self, request, queryset):

        if 'apply' in request.POST:
            for cuota in queryset:
                descripcion = request.POST["descripcion"]
                id_metodo = request.POST["metodo_de_pago"]
                metodo_pago = MetodoPago.objects.get(id=id_metodo)
                if metodo_pago:
                    cuota.metodo_pago = metodo_pago
                    cuota.referencia = descripcion
                    cuota.estado = 'P'
                    cuota.save()

            self.message_user(request, "Cambio de estado en {} cuotas".format(queryset.count()))
            return HttpResponseRedirect(request.get_full_path())
        
        form = RegistroPagoForm(initial={'_selected_action': queryset.values_list('id', flat=True)})
        return render(request, "cuota/pagocuota.html", {'items': queryset, 'form': form})
        

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

