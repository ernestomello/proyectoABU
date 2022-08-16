from calendar import month, month_name
from unittest.mock import DEFAULT
from django.db import models

# Create your models here.

class Persona(models.Model):
    # id_persona = models.AutoField(primary_key=True)
    identificacion = models.CharField(max_length=45,unique=True)
    nombre = models.CharField(max_length=45)
    apellido_paterno = models.CharField(max_length=45)
    apellido_materno = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    correo_electronico = models.EmailField()

    def __str__(self):
        return "{}, {}".format(self.nombre,self.apellido_paterno)


class Categoria_socio(models.Model):
    #id_categoria = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=30)
    importe_cuota = models.IntegerField()

    def __str__(self):
        return self.descripcion

class Socio(models.Model):
    FRECUENCIA_PAGOS = [
        ('ME','MENSUAL'),
        ('SE','SEMESTRAL'),
        ('AN','ANUAL'),
    ]
    id_socio = models.AutoField(primary_key=True)
    id_persona = models.OneToOneField(Persona, on_delete=models.CASCADE,blank=True,null=True)
    fecha_ingreso = models.DateField(verbose_name="Fecha de Ingreso")
    fecha_baja = models.DateField(verbose_name="Fecha de Baja")
    fecha_reingreso = models.DateField(verbose_name="Fecha de Reingreso")
    frecuencia_pago = models.CharField(max_length=2, choices=FRECUENCIA_PAGOS,default='ME')
    categoria_socio = models.ForeignKey(Categoria_socio,on_delete=models.CASCADE, verbose_name="Categoria Socio")
    def __str__(self):
        return "{}".format(self.id_persona)

class Cuota(models.Model):
    ESTADO_CUOTA = [
        ('P','PAGA'),
        ('N','NO PAGA')
    ]
    id_socio = models.ForeignKey(Socio, on_delete=models.RESTRICT)
    estado = models.CharField(max_length=1,choices=ESTADO_CUOTA,default='N')
    mes_anio = models.DateField(verbose_name="Mes-Año",)
    fecha_generada = models.DateField(auto_now_add=True)
    fecha_vencimiento  = models.DateField()

    def anio_mes(self):
        return "{}/{}".format(self.mes_anio.month,self.mes_anio.year)

