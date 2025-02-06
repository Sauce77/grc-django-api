from django.urls import path

from .views import root, mostrar_registros, actualizar_registros

urlpatterns = [
    path('', root),
    path("registros/<str:app>/", mostrar_registros, name="mostrar_registros"),
    path("insertar/", actualizar_registros, name="actualizar_registros")
]
