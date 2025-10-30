from django.db import models

# Create your models here.
class Direccion(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    calle = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    piso = models.CharField(max_length=10, blank=True, null=True)
    otros = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.DecimalField(max_digits=5, decimal_places=0)
    pais = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.calle}, {self.ciudad}, {self.pais}"
    
class Socio(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    telefono = models.DecimalField(max_digits=9, decimal_places=0)
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    menor_edad = models.BooleanField()
    IBAN = models.CharField(max_length=34, blank=True, null=True)
    documento_identidad = models.CharField(max_length=9, unique=True, null=True)
    
    def __str__(self):
        return self.nombre