from django.urls import path

from .views import root,RegistroList, RegistroDetail

urlpatterns = [
    path('', root),
    path("registros/", RegistroList.as_view()),
    path("registro/<int:pk>", RegistroDetail.as_view()),
]
