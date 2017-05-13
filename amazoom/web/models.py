from django.db import models


class Product(models.Model):
	name = models.CharField('Nombre', max_length=255)
	description = models.CharField('Descripción', max_length=1023)
	price = models.FloatField('Precio')

	def __str__(self):
		return self.name
