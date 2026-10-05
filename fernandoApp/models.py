from django.db import models

# Create your models here.

from django.db import models

class Paciente(models.Model):
    run = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()

    class Meta:
        db_table = 'pacientes'
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.run})"