from django.db import models
from django.contrib.auth.models import User

class MovimientoCaja(models.Model):
    TIPO_MOVIMIENTO = [
        ('E','ENTRADA'),
        ('S','SALIDA')
    ]
    TIPO_CAJA = [
        ('S','Secretaria'),
        ('T','Tesoreria')
    ]
    
    fecha = models.DateField()
    motivo = models.CharField(max_length=200)
    importe = models.DecimalField(decimal_places=2,max_digits=10)
    tipo_movimiento = models.CharField(max_length=1,choices=TIPO_MOVIMIENTO)
    tipo_caja = models.CharField(max_length=1,choices=TIPO_CAJA)
    user = models.ForeignKey(User,null=True, blank=True,on_delete=models.SET_NULL)
    
    def __str__(self) -> str:
        return "{}".format(self.motivo)