from datetime import datetime
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from socios.models import Cuota, MetodoPago, Persona, Socio
from socios.serializers import SocioSerializer,PersonaSerializer,CuotaSerializer,CuotaSolaSerializer, MetodoPagoSerializer
from datetime import date

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


@api_view(['GET',])
def genera_cuotas(request):
    """
    Genera las cuotas de un mes para todos los socios de Alta
    """
    if request.method == 'GET':
        socios_alta = Socio.objects.filter(estado='A')
        if socios_alta:
            for socio in socios_alta:
                cuota = Cuota(
                    id_socio= socio,
                    mes_anio=date.today(),
                    fecha_vencimiento=date.today(),
                    importe=socio.importe_cuota()
                )
                cuota.save()
    content ={'Respuesta':'Generadas las Cuotas'}
    return Response(content,status=status.HTTP_201_CREATED)
    

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
