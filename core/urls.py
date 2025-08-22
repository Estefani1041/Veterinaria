from django.urls import path
from core import  views

urlpatterns = [
    path("", views.login, name="login"),
    path("home/", views.home, name="home"),
    path('cerrar/', views.cerrar_sesion, name='cerrar'),
]