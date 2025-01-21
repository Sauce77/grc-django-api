from django.shortcuts import render,HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

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