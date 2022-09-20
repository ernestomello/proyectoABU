from django.contrib import admin,messages
from daterangefilter.filters import  FutureDateRangeFilter
from cajas.models import MovimientoCaja
# Register your models here.

class MovimientoCajaAdmin(admin.ModelAdmin):
    list_display = ('fecha','motivo','importe','tipo_movimiento','tipo_caja','user')
    list_filter = (('fecha',FutureDateRangeFilter),'tipo_movimiento','tipo_caja')
    exclude = ['user',]
     
    def save_model(self, request, obj, form, change):
        if not obj.id:
        # Only set added_by during the first save.
            obj.user = request.user
        if obj.user == request.user or request.user.is_superuser:
            super(MovimientoCajaAdmin,self).save_model(request, obj, form, change)
        else:
            self.message_user(request, 'Solo el usuario "{}" puede modificar este registro'.format(obj.user), level=messages.WARNING)
    
            
        
admin.site.register(MovimientoCaja,MovimientoCajaAdmin)