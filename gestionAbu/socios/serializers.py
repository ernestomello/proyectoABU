from socios.models import MetodoPago, Socio,Persona,Cuota,Categoria_socio
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from rest_framework import routers,serializers,viewsets



class Categoria_socioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria_socio
        fields = ['descripcion']

class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = ['descripcion']

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields =['nombre','apellido_paterno','apellido_materno','fecha_nacimiento','direccion','telefono']

class SocioSerializer(serializers.ModelSerializer):
    id_persona = PersonaSerializer(
        many=False,
        read_only= True
    )
    categoria_socio = Categoria_socioSerializer(
        many=False,
        read_only= True
    )
    frecuencia_pago = serializers.SerializerMethodField()
    estado = serializers.SerializerMethodField()
    class Meta:
        model = Socio
        fields =['id_socio','id_persona','categoria_socio','frecuencia_pago','estado']
    def get_frecuencia_pago(self, obj):
        return obj.get_frecuencia_pago_display()
    def get_estado(self, obj):
        return obj.get_estado_display()

class SocioNombreSerializer(serializers.ModelSerializer):
    class Meta:
        model= Socio
        fields = ['id_persona']
    def get_id_persona(self,obj):
        return obj.get_id_persona_display()

class CuotaSerializer(serializers.ModelSerializer):

    estado = serializers.SerializerMethodField()
    metodo_pago = MetodoPagoSerializer(
        many=False,
        read_only=True
    )
    class Meta:
        model = Cuota
        fields = '__all__'
    
    def get_estado(self, obj):
        return obj.get_estado_display()
    

class CuotaSolaSerializer(serializers.ModelSerializer):

    estado = serializers.SerializerMethodField()
    class Meta:
        model = Cuota
        fields ='__all__'
    def get_estado(self, obj):
        return obj.get_estado_display()
      

        
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

        