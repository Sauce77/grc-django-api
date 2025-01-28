from django.urls import path

from .views import root,RegistroList, RegistroDetail, crear_registro, mostrar_registros

urlpatterns = [
    path('', root),
    path("registros/", RegistroList.as_view()),
    path("registro/<int:pk>", RegistroDetail.as_view()),
    path("registro/nuevo/", crear_registro, name="crear_registro"),
    path("registros/<str:app>/", mostrar_registros, name="mostrar_registros"),
]
