from datetime import datetime, timedelta
from django.contrib import messages, admin
from django.http import HttpResponse, FileResponse
import csv
import calendar

from socios.models import Socio, Categoria_socio,Cuota,MetodoPago
#from cuotas.models import Cuota
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import GenerarCuotaForm, RegistroPagoForm
from daterangefilter.filters import  FutureDateRangeFilter
from reportlab.pdfgen import canvas


class CuotaAdmin(admin.ModelAdmin):
    list_display = ('id_socio','estado','anio_mes','importe','fecha_pago','metodo_pago')
    search_fields = ('id_socio__id_persona__nombre','id_socio__id_persona__apellido_paterno',)
    list_filter = (('fecha_pago',FutureDateRangeFilter),'estado','anio_cuota','mes_cuota','metodo_pago',)
    list_per_page = 30
    actions = ['registro_pago','imprimir_pago']

    class Media:
        css = {"all": ("css/style.css",)}

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
                    cuota.fecha_pago = datetime.today()
                    cuota.save()

            self.message_user(request, "Cambio de estado en {} cuotas".format(queryset.count()))
            return HttpResponseRedirect(request.get_full_path())
        
        form = RegistroPagoForm(initial={'_selected_action': queryset.values_list('id', flat=True)})
        return render(request, "cuota/pagocuota.html", {'items': queryset, 'form': form})       

    @admin.action(description='Imprimir Reporte')
    def imprimir_pago(self, request, queryset):
        from io import BytesIO
 
        buffer = BytesIO()
        p = canvas.Canvas(buffer)
    
        # Create a PDF document
        # books = Book.objects.all()
        p.drawString(100, 750, "Prueba de Cuotas")
    
        y = 700
        # for book in books:
            
    
        
        #return buffer
        #if 'apply' in request.POST:
        for cuota in queryset:
            print(cuota.id_socio)
            #descripcion = request.POST["descripcion"]
            #id_metodo = request.POST["metodo_de_pago"]
            #metodo_pago = MetodoPago.objects.get(id=id_metodo)
            p.line(0,y +12,1000,y +12)
            p.drawString(100, y, f"Socio: {cuota.id_socio}")
            p.drawString(100, y - 20, f"Importe: {cuota.importe}")
            p.drawString(100, y - 40, f"Cuota: {cuota.anio_cuota}/{cuota.mes_cuota}")
            y -= 60
            """ if metodo_pago:
                cuota.metodo_pago = metodo_pago
                cuota.referencia = descripcion
                cuota.estado = 'P'
                cuota.fecha_pago = datetime.today()
                cuota.save() """
            
        p.showPage()
        p.save()
    
        buffer.seek(0)
        #self.message_user(request, "Cambio de estado en {} cuotas".format(queryset.count()))
        #return HttpResponseRedirect(request.get_full_path())
        return FileResponse(buffer, as_attachment=True, filename="hello.pdf")
    
        # form = RegistroPagoForm(initial={'_selected_action': queryset.values_list('id', flat=True)})
        # return render(request, "cuota/pagocuota.html", {'items': queryset, 'form': form})        

admin.site.register(Cuota,CuotaAdmin)


admin.site.register(MetodoPago)


class SocioAdmin(admin.ModelAdmin):
    #inlines = (CursoInLine,)
    list_display    = ('id_persona','estado','categoria_socio','frecuencia_pago','deuda_socio','contacto')
    list_filter     = ('categoria_socio','frecuencia_pago','estado',)
    search_fields   = ('id_persona__nombre','id_persona__apellido_paterno',)
    actions         = ['generar_cuota']
    fields          = ('id_persona',('estado','fecha_ingreso'), 'fecha_baja','fecha_reingreso','frecuencia_pago',('categoria_socio','importe_cuota_jubilado'))
    list_per_page   = 30

    @admin.action(description='Generar Cuota')
    def generar_cuota(self, request, queryset):

        if 'apply' in request.POST:
            #print(queryset)
            year_init   = request.POST["fecha_desde_year"]
            year_end    = request.POST["fecha_hasta_year"]
            month_init  = request.POST["fecha_desde_month"]
            month_end   = request.POST["fecha_hasta_month"]
            if fecha_inconsistente(year_init, month_init, year_end, month_end):
                self.message_user(request, "Fechas inconsistente, no se generaron cuotas nuevas.", level=messages.ERROR)
            else:
                rango_fechas = range_month(year_init, month_init, year_end, month_end)
                cantidad=0
                for socio in queryset:
                    for fecha_valor in rango_fechas:
                        mes_ultima_cuota = socio.ultima_cuota_generada()
                        if mes_ultima_cuota == "":
                            mes_ultima_cuota = fecha_valor
                        else:
                            mes_ultima_cuota = add_months(mes_ultima_cuota,1)
                        if fecha_valor == mes_ultima_cuota:                     
                            cuota = Cuota.objects.get_or_create(
                                id_socio = socio,
                                mes_cuota =fecha_valor.month,
                                anio_cuota = fecha_valor.year,
                                mes_anio = fecha_valor,
                                fecha_vencimiento = fecha_valor + timedelta(days=10),
                                importe = socio.importe_cuota()
                            )
                            if cuota:
                                cantidad+= 1
                        #print(cuota)

                self.message_user(request, "Se generaron {} cuotas".format(cantidad))
            return HttpResponseRedirect(request.get_full_path())

        form = GenerarCuotaForm(initial={'_selected_action': queryset.values_list('id_socio', flat=True)})
        return render(request, "generar-cuota/generar_cuota.html", {'items': queryset, 'form': form})

    class Media:
        css = {"all": ("css/style.css",)}
def range_month(year_ini,month_ini,year_end,month_end):
    range_date = []
    dif_year = int(year_end) - int(year_ini)
    cant_moth = (12 * dif_year) + int(month_end) - int(month_ini)  + 1

    for i in range(int(month_ini),(int(month_ini)+cant_moth)):
        month_end = i % 12 #i-((i//12) * 12)
        if month_end == 0:
            month_end = 12
            j = 0
        else:
            j = i//12
        date_str = str(int(year_ini) +(j))+"-"+str(month_end)+"-01"
        range_date.append(datetime.strptime(date_str,"%Y-%m-%d").date())
    return range_date

def fecha_inconsistente(year_ini,month_ini,year_end,month_end):
    if year_ini > year_end:
        return True
    if year_ini == year_end and month_ini > month_end:
        return True
    return False       

def add_months(sourcedate, months):
    import datetime
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)

    
admin.site.register(Socio,SocioAdmin)

class CategoriaSocioAdmin(admin.ModelAdmin):
    list_display = ('descripcion','importe_cuota','voluntad')
admin.site.register(Categoria_socio,CategoriaSocioAdmin)



#class PagoCuotaAdmin(admin.ModelAdmin):
    #list_display = ('id_cuota__id_socio__nombre',)
#    pass

#admin.site.register(PagoCuota,PagoCuotaAdmin)




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





