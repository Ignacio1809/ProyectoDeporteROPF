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

class cliente(models.Model):
    telefono= models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    estatura= models.FloatField()
    peso = models.FloatField()
    imc = models.FloatField()
    fecha_nac= models.DateField()
    passwrd= models.CharField(max_length=12) 
    def __str__(self):
        return self.email