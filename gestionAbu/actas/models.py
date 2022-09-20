from tabnanny import verbose
from socios.models import Socio
from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
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
    class Meta:
        verbose_name_plural = 'Descriptores en Acta'

class ActaSocio(models.Model):
    id_acta = models.ForeignKey(Acta, on_delete=models.RESTRICT)
    id_socio = models.ForeignKey(Socio, on_delete=models.RESTRICT)
    class Meta:
        verbose_name_plural = 'Socios en Acta'