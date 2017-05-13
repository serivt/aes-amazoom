from django.db import models


class Shipping(models.Model):
	product = models.CharField(max_length=2023)
	direccion = models.CharField(max_length=2023)
	amount = models.IntegerField()
	total_price = models.FloatField()

	def __str__(self):
		return self.name

	@property
	def precio(self):
		return self.total_price / self.amount

	@precio.setter
	def precio(self, precio):
		self.total_price = precio * self.amount
