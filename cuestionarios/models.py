from django.db import models

# Create your models here.

class Tema(models.Model):
	nombre=models.CharField(max_length=100)
	def __str__(self):
		return self.nombre
	class Meta:
		ordering=['nombre']	

class Reactivo(models.Model):
	pregunta=models.TextField(blank=False, null=False)
	respuesta=models.TextField(blank=False, null=False)
	tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
	class Meta:
		verbose_name = 'Reactivo'
		verbose_name_plural='Reactivos'
	def __str__(self):
		return self.pregunta	