from rest_framework import serializers

from .models import Aplicativo, Perfil, Responsable, Registro

class PostRegistroSerializer(serializers.ModelSerializer):
    """
        Serializa la informacion para insertar un registro.
    """
    app = serializers.CharField(max_length=100,required=True)
    responsable = serializers.CharField(max_length=100,required=True)
    perfil = serializers.CharField(max_length=100,allow_blank=True,allow_null=True)

    class Meta:
        model = Registro
        exclude = ["id"]

class GetRegistroSerializer(serializers.ModelSerializer):
    """
        Serializa la informacion para mostrar un registro.
    """
    

    class Meta:
        model = Registro
        exclude = ["id"]