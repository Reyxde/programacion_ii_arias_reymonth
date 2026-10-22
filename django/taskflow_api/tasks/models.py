from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class control_vuelos(models.Model):
    id_vuelo = models.CharField(max_length=100)
    h_salida = models.TimeField
    h_llegada = models.TimeField
    destino= models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id_vuelo
