from rest_framework import serializers

from .models import Aplicativo, Perfil, Responsable, Registro

class RegistroSerializer(serializers.ModelSerializer):

    app = serializers.PrimaryKeyRelatedField(queryset=Aplicativo.objects.all())
    perfil = serializers.PrimaryKeyRelatedField(queryset=Perfil.objects.all(),allow_null=True,required=False)
    responsable = serializers.PrimaryKeyRelatedField(queryset=Responsable.objects.all())

    class Meta:
        model = Registro
        fields = "__all__"