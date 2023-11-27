from django.shortcuts import render, redirect
from .models import Product, Category, Cart, CartItem, Cart_Info
from django.http import JsonResponse
import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def docs(request):
	return render(request,'docs.html', {})


@login_required(login_url='/owner/login_user')
def home(request):
	
	category_1 = 'Glasses'
	category_2 = 'Watches'
	category_3 = 'Shirts'

	get_1 = Category.objects.get(name=category_1)
	get_2 = Category.objects.get(name=category_2)
	get_3 = Category.objects.get(name=category_3)

	products_1 = Product.objects.filter(category=get_1)
	products_2 = Product.objects.filter(category=get_2)
	
	products_3 = Product.objects.filter(category=get_3)
	
	if request.user.is_authenticated:
		cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
	
	products_2 = Product.objects.filter(category=get_2)
	products_3 = Product.objects.filter(category=get_3)
	return render(request, 'home.html', {'products_1':products_1, 'products_2':products_2, 'products_3':products_3, 'cart':cart})

@login_required(login_url='/owner/login_user')
def add_to_cart(request):
	data = json.loads(request.body)
	product_id = data['id']
	product = Product.objects.get(id=product_id)
	if request.user.is_authenticated:
		cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
		cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)

		cart_id = str(cart.id)

		if Cart_Info.objects.filter(cart_id=cart_id).exists():
			pass
		else:
			info = Cart_Info.objects.create(cart_id=cart_id, user=request.user.username)
			info.save()
		
		
		print(cartitem)
		cartitem.quantity += 1
		cartitem.save()
		num_of_item = cart.num_of_items
	return JsonResponse(num_of_item, safe=False)


@login_required(login_url='/owner/login_user')
def cart(request):
	cart = None
	cartitems = []

	if request.user.is_authenticated:
		cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
		

		cartitems = cart.cart_items.all()

	return render(request, 'cart.html', {'cart':cart, 'cartitems':cartitems})

@login_required(login_url='/owner/login_user')
def contact(request):
	
	return render(request, 'contact.html', {})



def confirm_payment(request, pk):
	cart = Cart.objects.get(id=pk)
	x=cart.id
	cart.completed = True


	person_id = str(x)
	info = Cart_Info.objects.get(cart_id=person_id)
	info.payment_status = True
	info.price_total += cart.total_price
	info.price_total2 += info.price_total
	info.save()
	cart.save()
	messages.success(request, 'Payments Made Successfully')
	print('Hi')
	return redirect('/owner')

