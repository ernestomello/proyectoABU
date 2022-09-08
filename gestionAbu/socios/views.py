from datetime import datetime,timedelta
import json
from sqlite3 import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from socios.models import Cuota, MetodoPago, Persona, Socio
from socios.serializers import SocioSerializer,PersonaSerializer,CuotaSerializer,CuotaSolaSerializer, MetodoPagoSerializer


@csrf_exempt
@api_view(['GET',])
def socio_list(request):
    """
    Lista todos los socios 
    """
    if request.method == 'GET':
        socios = Socio.objects.all()
        serializer = SocioSerializer(socios, many =True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(['GET',])
def persona_list(request):
    """
    Lista todos las personas
    """
    if request.method == 'GET':
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many =True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def socio_detail(request,pk):
    """
    Devuelve un socio por su id
    """
    try:
        socio = Socio.objects.get(pk = pk)
    except Socio.DoesNotExist:
        return  HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SocioSerializer(socio)
        return JsonResponse(serializer.data)

@csrf_exempt
def persona_detail(request,pk):
    """
    Devuelve un persona por su id
    """
    try:
        socio = Persona.objects.get(pk = pk)
    except Persona.DoesNotExist:
        return  HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PersonaSerializer(socio)
        return JsonResponse(serializer.data)
@csrf_exempt
def cuota_detail(request,id):
    """
    Devuelve las cuotas de un  socio por el id_socio
    """
    try:
        cuota = Cuota.objects.filter(id_socio = id).order_by('-mes_anio')
    except Cuota.DoesNotExist:
        return  HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CuotaSolaSerializer(cuota, many =True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(['PUT',])
def cuota_pago(request,id):
    """
    Paga una cuota según su id
    """
    

    if request.method == 'PUT':
        try:
            cuota = Cuota.objects.get(pk = id)
        except Cuota.DoesNotExist:
            return  HttpResponse(status=404)

        body = json.loads(request.body)
        data  = body[0]
        for key,value in data.items():
            if hasattr(cuota,key):
                if key == 'metodo_pago':
                    #print('paso metodo pago')
                    metodo_pago = MetodoPago.objects.get(pk =value)
                    setattr(cuota,key,metodo_pago)
                elif key == 'id_socio':
                        id_socio = Socio.objects.get(pk =value)
                        setattr(cuota,key,id_socio)
                else:
                    setattr(cuota,key,value)
        setattr(cuota,'estado','P')
        cuota.save()
        return Response({'Respuesta':'Cuota Actualizada'},status=status.HTTP_204_NO_CONTENT)



@csrf_exempt
@api_view(['GET',])
def cuota_list(request):
    """
    Lista todas las Cuotas 
    """
    if request.method == 'GET':
        socios = Cuota.objects.all().order_by('-mes_anio')
        serializer = CuotaSolaSerializer(socios, many =True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET',])
def metodo_pago_list(request):
    """
    Lista todas los metodos de pago
    """
    if request.method == 'GET':
        metodos = MetodoPago.objects.all()
        serializer = MetodoPagoSerializer(metodos, many =True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(['POST',])
def genera_cuotas(request):
    """
    Genera las cuotas de un mes para todos los socios de Alta
    ---
    list:
        parameters:  
            - id_socio: id_socio
            - fecha_desde: fecha desde
    
    """
    cantidad = 0
    
    if request.method == 'POST':
        socios_alta =[]
        body = json.loads(request.body)
        data  = body[0]
        socios = data['id_socio']
        fecha_desde = datetime.strptime(data['fecha_desde'],"%Y-%m-%d").date()
        fecha_hasta = datetime.strptime(data['fecha_hasta'],"%Y-%m-%d").date()
        rango_fechas = range_month(data['fecha_desde'],data['fecha_hasta'])
       
        if socios == 0:
            socios_alta = Socio.objects.filter(estado='A')
        else:
            socios_alta.append(Socio.objects.get(pk=socios))
            #print(socios_alta)
        
        if socios_alta:   
            
            for socio in socios_alta:
                #print(socio)
                if cuota_siguiente(socio,data['fecha_desde']):    
                    for fecha_valor in rango_fechas:                    
                        cuota = Cuota.objects.get_or_create(
                            id_socio = socio,
                            mes_anio = fecha_valor,
                            fecha_vencimiento = fecha_valor + timedelta(days=10),
                            importe = socio.importe_cuota()
                        )
                        if cuota:
                            cantidad+= 1

    cantidad = "Se generaron {} cuotas".format(cantidad)
    content ={"Respuesta":cantidad}
    return Response(content,status=status.HTTP_201_CREATED)

def range_month(str_date_ini, str_date_end):
    range_date = []
    year_ini = int(str_date_ini[:4])
    year_end = int(str_date_end[:4])
    dif_year = year_end - year_ini
    month_ini = int(str_date_ini[5:7])
    cant_moth = (12 * dif_year) + int(str_date_end[5:7]) - month_ini  + 1

    for i in range(month_ini,(month_ini+cant_moth)):
        month_end = i-((i//12) * 12)
        if month_end == 0:
            month_end = 12
        date_str = str(year_ini +(i//12))+"-"+str(month_end)+"-01"
        range_date.append(datetime.strptime(date_str,"%Y-%m-%d").date())
    return range_date

def cuota_siguiente(socio,str_date_ini):
    #return True
    #""" 
    year_ini = int(str_date_ini[:4])
    month_ini = int(str_date_ini[5:7])
    str_date_ultima = socio.ultima_cuota_generada()
    print('{} ultima- {}/{}'.format(str_date_ultima,month_ini,year_ini))
    if str_date_ultima:
        year_ultima = int(str_date_ultima[:4])
        month_ultima = int(str_date_ultima[5:7])
        print('{} ultima- {}/{}'.format(str_date_ultima,month_ultima,year_ultima))
        if month_ultima == 12:
            if month_ini != 1:
                return False
            else:
                if year_ini != year_ultima +1:
                    return False
                else:
                    return True
        else:
            if year_ini == year_ultima:
                return True
            else:
                return False
    return True
    #"""