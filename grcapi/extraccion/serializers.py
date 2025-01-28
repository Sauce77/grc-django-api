from rest_framework import serializers

from .models import Aplicativo, Perfil, Responsable, Registro

class AppSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aplicativo
        exclude = ["id"]

class PerfilSerializer(serializers.ModelSerializer):

    class Meta:
        model = Perfil
        exclude = ["id"]

class ResponsableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Responsable
        exclude = ["id"]

class RegistroSerializer(serializers.ModelSerializer):

    app = AppSerializer()
    perfil = PerfilSerializer()
    responsable = ResponsableSerializer()

    class Meta:
        model = Registro
        fields = "__all__"