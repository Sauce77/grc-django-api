from django.shortcuts import render,HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

from .models import Registro

from .serializers import RegistroSerializer

def root(request):
    return(HttpResponse("root"))

class RegistroList(APIView):
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