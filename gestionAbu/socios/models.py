from calendar import month
from datetime import datetime
from pickletools import decimalnl_long
from pydoc import plain
from random import choices
from re import T
from tabnanny import verbose
from tkinter import Widget
from unicodedata import decimal
from unittest.mock import DEFAULT
from urllib import response
#from socios.views import cuotas_por_socio
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
import requests

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
        
class Persona(models.Model):
    """
    Representa las personas que luego pueden ser Socios o Funcionarios o Proveedores ....
    """
    identificacion = models.CharField(max_length=45,unique=True)
    nombre = models.CharField(max_length=45)
    apellido_paterno = models.CharField(max_length=45)
    apellido_materno = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField()
    departamento = models.ForeignKey(Departamento, on_delete=models.DO_NOTHING,blank=True,null=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    correo_electronico = models.EmailField()

    def descripcion(self):
        return "{}, {} {}".format(self.nombre,self.apellido_paterno,self.apellido_materno)

    def __str__(self):
        return "{}, {} {}".format(self.nombre,self.apellido_paterno,self.apellido_materno)


class Categoria_socio(models.Model):
    #id_categoria = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=30)
    importe_cuota = models.IntegerField()
    class Meta:
        verbose_name_plural = 'Categoría de Socios'

    def __str__(self):
        return self.descripcion

class Socio(models.Model):
    FRECUENCIA_PAGOS = [
        ('ME','MENSUAL'),
        ('SE','SEMESTRAL'),
        ('AN','ANUAL'),
    ]
    ESTADO_SOCIO =[
        ('A','ALTA'),
        ('B','BAJA'),
        ('R','REAFILIADO')
    ]
    id_socio = models.AutoField(primary_key=True)
    id_persona = models.OneToOneField(Persona, on_delete=models.DO_NOTHING,blank=True,null=True)
    fecha_ingreso = models.DateField(verbose_name="Fecha de Ingreso")
    estado = models.CharField(max_length=1,choices=ESTADO_SOCIO,default='A')
    fecha_baja = models.DateField(verbose_name="Fecha de Baja")
    fecha_reingreso = models.DateField(verbose_name="Fecha de Reingreso")
    frecuencia_pago = models.CharField(max_length=2, choices=FRECUENCIA_PAGOS,default='ME')
    categoria_socio = models.ForeignKey(Categoria_socio,on_delete=models.DO_NOTHING, verbose_name="Categoria Socio")
    def __str__(self):
        #return "{}, {}".format(self.id_persona.nombre,self.id_persona.apellido_paterno)
        return "{}".format(self.id_persona)
    
    def importe_cuota(self):
        return self.categoria_socio.importe_cuota
    
    class Meta:
        pass
    
    #@property
    def contacto(self):
        return "{} - {}".format(self.id_persona.celular, self.id_persona.correo_electronico)

    def deuda_socio(self):
        """ url_root = settings.ALLOWED_HOSTS
        port = settings.ALLOWED_PORT
        response = requests.get("http://{}:{}/socios/{}".format(url_root[0],port[0],self.id_socio)+"/cuotas")
        cuotas = response.json()
        #cuotas = cuotas_por_socio(self.id_socio) """
        cuotas = Cuota.objects.filter(id_socio=self).order_by('-mes_anio')
        importe_total = 0.00
        mes_anio = ""
        for cuota in cuotas:
            if cuota.estado != "P":
                importe_total  += cuota.importe
            else:
                mes_anio = cuota.mes_anio
        if mes_anio == "":
            mes_anio = datetime.strftime(mes_anio,"%d-%m-%Y").date()
        else:
            mes_anio = mes_anio.strftime("%d/%m/%Y")
        return "$ {} ({})".format(importe_total,mes_anio)

    def ultima_cuota_generada(self):
        """ url_root = settings.ALLOWED_HOSTS
        port = settings.ALLOWED_PORT
        response = requests.get("http://{}:{}/socios/{}".format(url_root[0],port[0],self.id_socio)+"/cuotas")
        cuotas = response.json() """
        cuotas = Cuota.objects.filter(id_socio=self).order_by('-anio_mes')
        mes_anio = ""
        if cuotas: 
            mes_anio = cuotas[0]['mes_anio']          
            """
            for cuota in cuotas:
                if cuota['estado'] == "PAGA":
                    mes_anio = cuota['mes_anio']
            print(mes_anio)
            """   
        
        return "{}".format(mes_anio)


    """ def get_fields(self, request, obj=None):
        fs = [
            (self.label,  {'fields': ['id_socio',]}),
            ('Map', {'fields': [], # required by django admin
                    'description':obj.ultima_cuota_paga(),
            }),
        ]
        return fs """

        
class MetodoPago(models.Model):
    """
    Forma de pago definida para una cuota
    """
    descripcion = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'Método de Pago'
    def __str__(self):
        return "{}".format(self.descripcion)

class Cuota(models.Model):
    ESTADO_CUOTA = [
        ('P','PAGA'),
        ('N','NO PAGA')
    ]
    id_socio = models.ForeignKey(Socio, on_delete=models.RESTRICT)
    estado = models.CharField(max_length=1,choices=ESTADO_CUOTA,default='N')
    importe = models.FloatField(default=0.00)
    mes_anio = models.DateField(verbose_name="Mes-Año")
    fecha_generada = models.DateField(auto_now_add=True)
    fecha_vencimiento  = models.DateField()
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.RESTRICT,default=None,blank=True,null=True)
    referencia = models.CharField(max_length=200,default=None,blank=True,null=True)
    
    def anio_mes(self):
        return "{}/{}".format(self.mes_anio.month,self.mes_anio.year)
    def __str__(self):
        return "{}, {}-{}".format(self.id_socio.id_persona.nombre,self.id_socio.id_persona.apellido_paterno,self.anio_mes())
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_socio','mes_anio'],name='unique_socio_cuota')
        ]
        
class PagoCuota(models.Model):
    """
    Pensada para cuando la cuota se puede pagar con varios meotodos de pago
    """
    id_cuota = models.OneToOneField(Cuota,on_delete=models.RESTRICT)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.RESTRICT)
    referencia = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = 'Pago de Cuotas'

class Descriptor(models.Model):
    """
    Para representar los descriptores que tendrán las Actas
    """
    palabra_clave = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'Descriptores'

    def __str__(self):
        return "{}".format(self.palabra_clave)

class Acta(models.Model):
    fecha = models.DateField()
    asunto = models.CharField(max_length=50,default="")
    contenido = RichTextField(max_length=5000)

    def __str__(self):
        return "{}".format(self.asunto)

class ActaDescriptor(models.Model):
    acta = models.ForeignKey(Acta, on_delete=models.RESTRICT)
    descriptor = models.ForeignKey(Descriptor, on_delete=models.RESTRICT)
   

class ActaSocio(models.Model):
    id_acta = models.ForeignKey(Acta, on_delete=models.RESTRICT)
    id_socio = models.ForeignKey(Socio, on_delete=models.RESTRICT)


class TipoFormacion(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self) -> str:
        return "{}".format(self.descripcion)

class Formacion(models.Model):
    id_persona = models.ForeignKey(Persona,on_delete=models.RESTRICT)
    tipo_formacion = models.ForeignKey(TipoFormacion,on_delete=models.RESTRICT)
    titulo = models.CharField(max_length=100)
    fecha_titulo = models.DateField(verbose_name= 'Fecha del Titulo')
    institucion = models.CharField(max_length=100)
    duracion = models.CharField(max_length=50)
    plan = models.CharField(max_length=100)
    fecha_revalida = models.DateField()

    def __str__(self) -> str:
        return "{} - {}".format(self.tipo_formacion.descripcion,self.titulo)
    
    class Meta:
        verbose_name_plural = 'Formaciones'

class PerfilCargo(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self) -> str:
        return "{}".format(self.descripcion)

class LugarTrabajo(models.Model):
    id_persona = models.ForeignKey(Persona,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    perfil_cargo = models.ManyToManyField(PerfilCargo)
    fecha_ingreso = models.DateField()
    fecha_egreso = models.DateField()

    def __str__(self) -> str:
        return "{}".format(self.nombre)

    class Meta:
        verbose_name_plural = 'Lugares de Trabajo'
