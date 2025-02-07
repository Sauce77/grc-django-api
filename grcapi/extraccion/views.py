from django.shortcuts import render,HttpResponse
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from scripts.operaciones_registros import leer_registros

# Create your views here.

from .models import Registro

from .serializers import GetRegistroSerializer,PostRegistroSerializer

def root(request):
    return(HttpResponse("root"))        
    
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def mostrar_registros(request,app):
    """
        Muestra los registros de una app.
    """
    registros = Registro.objects.filter(app__nombre=app)
    serializer = GetRegistroSerializer(registros, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsAdminUser])
def actualizar_registros(request):
    """
        Recibe una extraccion completa. Actualiza los datos ya existentes en la 
        base de datos y crea aquellos que no estan presentes.

        Para detectar los que no estan presentes, se recurre al atributo "en_extraccion",
        si es verdadero, el registro fue encontrado en la extraccion.
    """
    # colocamos el estado "en_extraccion" como false
    Registro.objects.all().update(en_extraccion=False)
    # recibe la extraccion
    leer_registros(request.data)
        
    return Response(status=status.HTTP_200_OK)

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def mostrar_no_extraccion(request):
    """
        Muestra los registros cuyo atributo "en_extraccion"=False
        Esto quiere decir que no se encontraron en la extraccion
        mas reciente
    """
    registros = Registro.objects.filter(en_extraccion=False)
    serializer = GetRegistroSerializer(registros, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)