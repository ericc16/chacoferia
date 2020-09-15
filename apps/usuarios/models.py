from django.db import models

# Create your models here.

class Perfil(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField(max_length=8,primary_key=True)
    tel = models.PositiveIntegerField(max_length=12)
    domicilio = models.CharField(max_length=100)
    fechaNacimiento = models.DateField()

    def __str__(self):
        text = "{0} , {1}"
        return text.format(self.nombre,self.apellido)
    
    class Meta:
        db_table = 'perfil'
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['id']