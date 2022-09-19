from django import forms

from .models import MetodoPago

class RegistroPagoForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    descripcion = forms.CharField()
    metodo_de_pago = forms.ModelChoiceField(MetodoPago.objects.all(), required=True)

class GenerarCuotaForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    fecha_desde = forms.DateField( widget = forms.SelectDateWidget)
    fecha_hasta = forms.DateField( widget = forms.SelectDateWidget)
