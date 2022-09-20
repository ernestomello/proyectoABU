
from email.headerregistry import Group
from pickletools import decimalnl_long
from pydoc import plain
from random import choices
from re import T
from tabnanny import verbose
from unicodedata import decimal
from unittest.mock import DEFAULT
#from socios.views import cuotas_por_socio
from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages
from personas.models import Persona
from datetime import datetime
#from cuotas.models import Cuota

# Create your models here.




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
        ('B','BAJA')
    ]
    id_socio = models.AutoField(primary_key=True)
    id_persona = models.OneToOneField(Persona, on_delete=models.DO_NOTHING,blank=True,null=True, verbose_name="Nombre")
    fecha_ingreso = models.DateField(verbose_name="Fecha de Ingreso")
    estado = models.CharField(max_length=1,choices=ESTADO_SOCIO,default='A')
    fecha_baja = models.DateField(verbose_name="Fecha de Baja",blank=True,null=True)
    fecha_reingreso = models.DateField(verbose_name="Fecha de Reingreso",null=True,blank=True)
    frecuencia_pago = models.CharField(max_length=2, choices=FRECUENCIA_PAGOS,default='ME')
    categoria_socio = models.ForeignKey(Categoria_socio,on_delete=models.DO_NOTHING, verbose_name="Categoria Socio")
    importe_cuota_jubilado = models.DecimalField(decimal_places=2,max_digits=10,blank=True,default=0.00)
    
    def __str__(self):
        return "{}".format(self.id_persona)
    
    def importe_cuota(self):
        return self.categoria_socio.importe_cuota
    
    class Meta:
        pass

    # def save(self, *args, **kwargs):
    #     if self.estado == "B" and self.fecha_baja is None:
    #         self
            
    #     if self.estado != "B":
    #         print("SE GUARDARON LOS CAMBIOS")
    #         super().save(*args, **kwargs)

        
        
    
    #@property
    def contacto(self):
        return "{} - {}".format(self.id_persona.celular, self.id_persona.correo_electronico)

    def deuda_socio(self):
        cuotas = Cuota.objects.filter(id_socio=self).order_by('-mes_anio')
        importe_total = 0.00
        mes_anio = ""
        for cuota in cuotas:
            if cuota.estado != "P":
                importe_total  += cuota.importe
            else:
                mes_anio = cuota.mes_anio
        if mes_anio == "":
            # mes_anio = datetime.strptime(mes_anio,"%d-%m-%Y").date()
            mes_anio =""
        else:
            mes_anio = mes_anio.strftime("%d/%m/%Y")
        return "$ {} ({})".format(importe_total,mes_anio)

    def ultima_cuota_generada(self):
        cuotas = Cuota.objects.filter(id_socio=self).order_by('-anio_mes')
        mes_anio = ""
        if cuotas: 
            mes_anio = cuotas.mes_anio         
        
        return "{}".format(mes_anio)
        
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
        if year_ini == year_end and month_ini > month_end:
            return True
        return False       

"""        
class PagoCuota(models.Model):
"""
    #Pensada para cuando la cuota se puede pagar con varios meotodos de pago
"""
    id_cuota = models.OneToOneField(Cuota,on_delete=models.RESTRICT)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.RESTRICT)
    referencia = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Pago de Cuotas'

"""




