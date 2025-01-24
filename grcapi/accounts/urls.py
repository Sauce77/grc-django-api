from django.urls import path

from .views import UserList, registro, login

urlpatterns = [
    path("users/", UserList.as_view()),
    path("registro/", registro, name="registro"),
    path("login/", login, name="login")
]
