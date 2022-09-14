from calendar import month
from datetime import datetime
from pickletools import decimalnl_long
from random import choices
from re import T
from tkinter import Widget
from unicodedata import decimal
from unittest.mock import DEFAULT
from urllib import response
#from socios.views import cuota_detail
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
    # id_persona = models.AutoField(primary_key=True)
    identificacion = models.CharField(max_length=45,unique=True)
    nombre = models.CharField(max_length=45)
    apellido_paterno = models.CharField(max_length=45)
    apellido_materno = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField()
    departamento = models.OneToOneField(Departamento, on_delete=models.DO_NOTHING,blank=True,null=True)
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
        url_root = settings.ALLOWED_HOSTS
        port = settings.ALLOWED_PORT
        response = requests.get("http://{}:{}/socios/{}".format(url_root[0],port[0],self.id_socio)+"/cuotas")
        cuotas = response.json()
        
        importe_total = 0.00
        mes_anio = ""
        for cuota in cuotas:
            if cuota['estado'] != "PAGA":
                importe_total  += cuota['importe']
            else:
                mes_anio = cuota['mes_anio']
        if mes_anio != "":
            mes_anio = datetime.strptime(mes_anio,"%Y-%m-%d").date()
        return "$ {} ({})".format(importe_total,mes_anio)

    def ultima_cuota_generada(self):
        url_root = settings.ALLOWED_HOSTS
        port = settings.ALLOWED_PORT
        response = requests.get("http://{}:{}/socios/{}".format(url_root[0],port[0],self.id_socio)+"/cuotas")
        cuotas = response.json()
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

    def range_month(year_ini,month_ini,year_end,month_end):
        range_date = []
        dif_year = int(year_end) - int(year_ini)
        cant_moth = (12 * dif_year) + int(month_end) - int(month_ini)  + 1

        for i in range(int(month_ini),(int(month_ini)+cant_moth)):
            month_end = i-((i//12) * 12)
            if month_end == 0:
                month_end = 12
            date_str = str(int(year_ini) +(i//12))+"-"+str(month_end)+"-01"
            range_date.append(datetime.strptime(date_str,"%Y-%m-%d").date())
        return range_date

    def fecha_inconsistente(year_ini,month_ini,year_end,month_end):
        if year_ini > year_end:
            return True
        if year_ini == year_end & month_ini > month_end:
            return True
        return False
        
class PagoCuota(models.Model):
    id_cuota = models.OneToOneField(Cuota,on_delete=models.RESTRICT)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.RESTRICT)
    referencia = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = 'Pago de Cuotas'

class Descriptor(models.Model):
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