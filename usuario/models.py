from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from personal.models import Personal


class Tipo(models.Model):
    TIPO_CARGO_CHOICES = [
        ('empleado', 'Empleado'),
        ('cliente', 'Cliente'),
        ('administrador', 'Administrador'),
    ]

    id = models.AutoField(primary_key=True)
    cargo = models.CharField(max_length=15, choices=TIPO_CARGO_CHOICES)

    class Meta:
        db_table = 'tipo'

    def __str__(self):
        return self.cargo   # ahora se muestra el cargo


class Usuario(models.Model):
    id_personal = models.ForeignKey(
        Personal, on_delete=models.CASCADE,
        db_column='id_empleado', null=True, blank=True
    )
    id_tipo = models.ForeignKey('Tipo', on_delete=models.CASCADE, db_column='id_tipo')
    usuario = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return self.usuario   # ahora se muestra el nombre de usuario

    # Guardar contraseña encriptada
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    # Verificar contraseña
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
