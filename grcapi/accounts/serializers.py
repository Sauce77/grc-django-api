from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ["id","nombre"]

class UserSerializer(serializers.ModelSerializer):

    rol = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["first_name","last_name","username", "email","password","rol"]