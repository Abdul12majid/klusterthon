from django.db import models 
from django.core.validators import MinLengthValidator
import datetime
import uuid
from django.contrib.auth.models import User

# Create your models here. Category, Cart, Product, Cartitem

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


	@property
	def total_price(self):
		cartitems = self.cart_items.all()
		total = sum([item.price for item in cartitems])
		return total

	@property
	def num_of_items(self):
		cartitems = self.cart_items.all()
		quantity = sum([item.quantity for item in cartitems])
		return quantity
		
	


class CartItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
	quantity = models.IntegerField(default=0)

	def __str__(self):
		return self.product.name

	@property
	def price(self):
		new_price = self.product.price * self.quantity
		return new_price


class Cart_Info(models.Model):
	cart_id = models.CharField(max_length=50)
	user = models.CharField(max_length=30)
	payment_status = models.BooleanField(default=False)
	price_total = models.IntegerField(default=0)
	price_total2 = models.IntegerField(default=0)
