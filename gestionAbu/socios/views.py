from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from socios.models import Cuota, Persona, Socio
from socios.serializers import SocioSerializer,PersonaSerializer,CuotaSerializer,CuotaSolaSerializer

@csrf_exempt
@api_view(['GET',])
def socio_list(request):
    """
    Lista todos los socios o crea un nuevo socio.
    """
    if request.method == 'GET':
        socios = Socio.objects.all()
        serializer = SocioSerializer(socios, many =True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(['GET',])
def persona_list(request):
    """
    Lista todos los socios o crea un nuevo socio.
    """
    if request.method == 'GET':
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many =True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def socio_detail(request,pk):
    """
    Devuelve un socio 
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
    Devuelve un socio 
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
    Devuelve las cuotas de un  socio 
    """
    try:
        cuota = Cuota.objects.filter(id_socio = id)
    except Cuota.DoesNotExist:
        return  HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CuotaSolaSerializer(cuota, many =True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(['GET',])
def cuota_list(request):
    """
    Lista todos los socios o crea un nuevo socio.
    """
    if request.method == 'GET':
        socios = Cuota.objects.all()
        serializer = CuotaSerializer(socios, many =True)
        return JsonResponse(serializer.data, safe=False)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
