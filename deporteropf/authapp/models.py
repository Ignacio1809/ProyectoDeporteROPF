from django.db import models

# Create your models here.
#en este archivo crearemos las tablas de nuestra base de datos 


class Plan(models.Model):
    nombre_plan = models.CharField(max_length=20)
    descripcion = models.TextField()
    precio = models.IntegerField()
    duracion =  models.CharField(max_length=20)
    beneficio= models.TextField()
    def __str__(self):
        return self.nombre_plan
