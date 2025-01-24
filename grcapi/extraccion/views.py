from django.shortcuts import render,HttpResponse
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.

from .models import Registro

from .serializers import RegistroSerializer

def root(request):
    return(HttpResponse("root"))

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def crear_registro(request):
    """
        Agrega un registro nuevo de extraccion a la base de datos.
    """
    serializer = RegistroSerializer(data=request.data, many=True)

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistroList(APIView):
    """
        Enlista los registros de la base de datos.
    """
    def get(self, request):
        registros = Registro.objects.all() 
        serializer = RegistroSerializer(registros, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        registro = RegistroSerializer(data=request.data)
        if registro.is_valid():
            registro.save()
            return Response(registro.data, status=status.HTTP_201_CREATED)
        
        return Response(registro.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RegistroDetail(APIView):
    """
        Selecciona un regsitro especifico con base en la llave primaria.
    """
    def get_registro(self,pk):
        try:
            return Registro.objects.get(pk=pk)
        except Registro.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        registro = self.get_registro(pk)
        serializer = RegistroSerializer(registro)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        registro = self.get_registro(pk)
        serializer = RegistroSerializer(registro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        registro = self.get_registro(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    