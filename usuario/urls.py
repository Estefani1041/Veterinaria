from django.urls import path
from . import views

urlpatterns = [
    path('gestionar_usuario', views.gestionar_usuario, name='gestionar_usuario'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('eliminar/', views.eliminar_usuario, name='eliminar_usuario'),
    path('actualizar/', views.actualizar_usuario, name='actualizar_usuario'),
    path('editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
]
