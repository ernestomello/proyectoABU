from django.db import models
from socios.models import Socio
from django.core.validators import MaxValueValidator,MinValueValidator


# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=200,verbose_name="Nombre del Curso")
    
    def __str__(self):
        return "{}".format(self.nombre)

class CursoSocio(models.Model):
    id_socio = models.ForeignKey(Socio, on_delete=models.RESTRICT, verbose_name="Nombre Socio")
    id_curso = models.ForeignKey(Curso, on_delete=models.RESTRICT,verbose_name="Materia que Cursa")
    anio = models.IntegerField(validators=[MaxValueValidator(2050), MinValueValidator(2000)], verbose_name="Año del Curso")
    importe_matricula = models.DecimalField(verbose_name="Cuota Inscripción",decimal_places=2,max_digits=10)
    pago_inscripcion = models.BooleanField(verbose_name="Pagó Inscripcion")
    def __str__(self):
        return "{}".format(self.id_curso)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_socio','id_curso','anio'],name='unique_socio_curso')
        ]
        verbose_name_plural = 'Matricula de Socios'
        verbose_name = "Matricula de Socio"