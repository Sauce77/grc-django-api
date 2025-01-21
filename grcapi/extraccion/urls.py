from django.urls import path

from .views import root,RegistroList

urlpatterns = [
    path('', root),
    path("registros/", RegistroList.as_view()),
]
