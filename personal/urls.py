from django.urls import path
from personal import  views

urlpatterns = [
    path("gestionar_personal/", views.gestionar_personal, name="gestionar_personal"),
    path("registrar_personal/", views.registrar_personal, name="registrar_personal"),
    path('eliminar/', views.eliminar_personal, name='eliminar_personal'),
    path('actualizar/<int:id>/', views.actualizar_personal, name='actualizar_personal'),  # esta línea es nueva
]

