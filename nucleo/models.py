from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



class Cliente(models.Model):
    dni=models.CharField(max_length=10)
    nombre=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    fechaNacimiento=models.DateField(blank=False)
    foto=models.ImageField(upload_to='photos/')
    idUsuario=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre+" "+self.apellidos


class Especialista(models.Model):
    dni=models.CharField(max_length=10)
    nombre=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    fechaNacimiento=models.DateField(blank=False)
    foto=models.ImageField(upload_to='photos/')
    biografia=models.CharField(max_length=255)
    idUsuario=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre+" "+self.apellidos


class cita(models.Model):
    fecha=models.DateField()
    idCliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idEspecialista=models.ForeignKey(Especialista, on_delete=models.CASCADE)
    informe=models.TextField()
    realizada=models.BooleanField(default=False)

    def __str__(self):
        return 'CLIENTE:'+" "+self.idCliente.nombre+" "+'ESPECIALISTA: '+" "+self.idEspecialista.nombre+" "+'FECHA: '+" "+self.fecha.strftime('%Y-%m-%d')

    class Meta:
        ordering = ['fecha']


class mensaje(models.Model):
    id_Emisor=models.ForeignKey(User, on_delete=models.CASCADE, related_name='id_Emisor')
    id_Receptor=models.ForeignKey(User, on_delete=models.CASCADE, related_name='id_Receptor')
    fecha=models.DateField(blank=False)
    asunto=models.CharField(max_length=50)
    texto=models.TextField()
    leido=models.BooleanField(default=False)

    def __str__(self):
        return self.idEmisor+" "+self.idReceptor+" "+self.asunto