#Se almacenan los modelos (una representacion de una tabla en la Base de Datos)

from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100) #tipo de dato que va aceptar ese atributo
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()

def __str__(self):
    return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"