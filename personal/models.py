from django.db import models

class Personal(models.Model):
    id = models.AutoField(db_column='id_empleado', primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)

    class Meta:
        db_table = 'personal'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
