from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Departamento(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    descripcion = models.CharField(max_length=50)
    
    def __str__(self):
        return self.descripcion

class Persona(models.Model):
    """
    Representa las personas que luego pueden ser Socios o Funcionarios o Proveedores ....
    """
    
    identificacion = models.CharField(max_length=45,unique=True)
    genero = models.ForeignKey(Genero, on_delete=models.DO_NOTHING,blank=True,null=True )
    nombre = models.CharField(max_length=45)
    apellido_paterno = models.CharField(max_length=45)
    apellido_materno = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField()
    departamento = models.ForeignKey(Departamento, on_delete=models.DO_NOTHING,blank=True,null=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    correo_electronico = models.EmailField()
    user = models.OneToOneField(User, null=True, blank=True,on_delete=models.SET_NULL)
    

    def nombre_completo(self):
        return "{}, {} {}".format(self.nombre,self.apellido_paterno,self.apellido_materno)

    def __str__(self):
        return "{}, {} {}".format(self.nombre,self.apellido_paterno,self.apellido_materno)

class TipoFormacion(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self) -> str:
        return "{}".format(self.descripcion)
    class Meta:
        verbose_name = 'Tipo de Formación'
        verbose_name_plural = 'Tipo de Formaciones'

class Formacion(models.Model):
    id_persona = models.ForeignKey(Persona,on_delete=models.RESTRICT)
    tipo_formacion = models.ForeignKey(TipoFormacion,on_delete=models.RESTRICT,verbose_name='Tipo de Formación')
    titulo = models.CharField(max_length=100)
    fecha_titulo = models.DateField(verbose_name= 'Fecha del Título')
    institucion = models.CharField(max_length=100)
    duracion = models.CharField(max_length=50)
    plan = models.CharField(max_length=100)
    fecha_revalida = models.DateField(verbose_name="Fecha de Reválida",null=True,blank=True)

    def __str__(self) -> str:
        return "{} - {}".format(self.tipo_formacion.descripcion,self.titulo)
    
    class Meta:
        verbose_name_plural = 'Formaciones'

class PerfilCargo(models.Model):
    descripcion = models.CharField(max_length=200)

    class Meta:
        verbose_name='Perfil del Cargo'
        verbose_name_plural = 'Perfiles del Cargo'

    def __str__(self) -> str:
        return "{}".format(self.descripcion)

class LugarTrabajo(models.Model):
    id_persona = models.ForeignKey(Persona,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    perfil_cargo = models.ManyToManyField(PerfilCargo,verbose_name='Perfiles del Cargo')
    fecha_ingreso = models.DateField()
    fecha_egreso = models.DateField(verbose_name="Fecha de Egreso",null=True,blank=True)

    def __str__(self) -> str:
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = 'Lugar de Trabajo'
        verbose_name_plural = 'Lugares de Trabajo'