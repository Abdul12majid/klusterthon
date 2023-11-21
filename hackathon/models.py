from django.db import models
from django.core.validators import MinLengthValidator
import datetime
import uuid

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=50, validators=[MinLengthValidator(3)])

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Categories'

class Customer(models.Model):
	first_name = models.CharField(max_length=30, validators=[MinLengthValidator(3)], null=False, blank=False)
	last_name = models.CharField(max_length=30, validators=[MinLengthValidator(3)], null=False, blank=False)
	phone = models.CharField(max_length=30, validators=[MinLengthValidator(3)], null=True, blank=True)
	email = models.EmailField(null=False, blank=False)
	password = models.CharField(null=False, blank=False, max_length=30, validators=[MinLengthValidator(3)])


class Product(models.Model):
	name = models.CharField(max_length=30, validators=[MinLengthValidator(3)], null=False, blank=False)
	price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
	description = models.CharField(max_length=250, validators=[MinLengthValidator(3)], null=True, blank=True)
	image = models.ImageField(upload_to='uploads/products')
	is_sale = models.BooleanField(default=False)
	sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

	def __str__(self):
		return self.name


class Cart(models.Model):
	id = models.UUIDField(default=uuid.uuid4, primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	completed = models.BooleanField(default=False)


class CartItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
	quantity = models.IntegerField(default=0)

	def __str__(self):
		return self.name