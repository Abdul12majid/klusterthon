from django.db import models

# Create your models here.
class Customer(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	name = models.CharField(max_length=30)
	paid = models.BooleanField(default=False)
