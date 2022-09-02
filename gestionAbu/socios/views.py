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
import pandas as pd 

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
        cuota = Cuota.objects.filter(id_socio = id)
    except Cuota.DoesNotExist:
        return  HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CuotaSerializer(cuota, many =True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(['GET',])
def cuota_list(request):
    """
    Lista todas las Cuotas 
    """
    if request.method == 'GET':
        socios = Cuota.objects.all()
        serializer = CuotaSerializer(socios, many =True)
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
    """
    cantidad = 0
    
    if request.method == 'POST':
        socios_alta =[]
        body = json.loads(request.body)
        data  = body[0]
        socios = data['id']
        fecha_desde = datetime.strptime(data['fecha_desde'],"%Y-%m-%d").date()
        fecha_hasta = datetime.strptime(data['fecha_hasta'],"%Y-%m-%d").date()
        
        rango_fechas = pd.date_range(fecha_desde,fecha_hasta,freq='MS')
        if socios == 0:
            socios_alta.append(Socio.objects.filter(estado='A'))
        else:
            socios_alta.append(Socio.objects.get(pk=socios))
        
        if socios_alta:            
            for socio in socios_alta:
                for fecha_valor in rango_fechas:
                    cuota = Cuota.objects.get_or_create(
                        id_socio= socio,
                        mes_anio=fecha_valor,
                        fecha_vencimiento=fecha_valor + timedelta(days=10),
                        importe=socio.importe_cuota()
                    )
                    if cuota:
                        cantidad+= 1
    cantidad = "Se generaron {} cuotas".format(cantidad)
    content ={"Respuesta":cantidad}
    return Response(content,status=status.HTTP_201_CREATED)
