from django.db import models

# Create your models here.

class Register (models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=30)
	
	def __str__(self):
		return self.email