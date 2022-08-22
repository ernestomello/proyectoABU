from socios.models import Socio,Persona,User
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from rest_framework import routers,serializers,viewsets

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields =['nombre','apellido_paterno','apellido_materno','fecha_nacimiento','direccion','telefono']

class SocioSerializer(serializers.ModelSerializer):
    id_persona = PersonaSerializer(
        many=False,
        read_only= True,
        #slug_field='descripcion'
    )
    class Meta:
        model = Socio
        fields =['id_socio','id_persona','categoria_socio']

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

        