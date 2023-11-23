from django.shortcuts import render, redirect
from .models import Product, Category, Cart, CartItem
from django.http import JsonResponse
import json
from django.contrib import messages

# Create your views here.
def home(request):
	messages.success(request, ('Payments Made Successfully'))
	category_1 = 'Glasses'
	category_2 = 'Watches'
	category_3 = 'Shirts'

	get_1 = Category.objects.get(name=category_1)
	get_2 = Category.objects.get(name=category_2)
	get_3 = Category.objects.get(name=category_3)

	products_1 = Product.objects.filter(category=get_1)
	products_2 = Product.objects.filter(category=get_2)
	x = 'Watches' == category_2
	print(x)
	products_3 = Product.objects.filter(category=get_3)
	
	if request.user.is_authenticated:
		cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
	
	products_2 = Product.objects.filter(category=get_2)
	products_3 = Product.objects.filter(category=get_3)
	return render(request, 'home.html', {'x':x, 'products_1':products_1, 'products_2':products_2, 'products_3':products_3, 'cart':cart})




'''
from django.contrib.auth.decorators import login_required


# Create your views here.
#@login_required(login_url='login-user')


def category(request, foo):
	foo = foo.replace('-', ' ')
	try:
		category = Category.objects.get(name=foo)
		products = Product.objects.filter(category=category)
		return render(request, 'commerce/category.html', {'products':products, 'category':category})
	except:
		messages.success(request, ("Category doesn't exist"))
		return redirect('home')



def cart(request):
	cart = None
	cartitems = []


	if request.user.is_authenticated:
		cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
		cartitems = cart.cart_items.all()

	return render(request, 'cart.html', 'cart':cart, 'cartitems':cartitems)

'''

def add_to_cart(request):
	data = json.loads(request.body)
	product_id = data['id']
	product = Product.objects.get(id=product_id)
	if request.user.is_authenticated:
		cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
		cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
		print(cartitem)
		cartitem.quantity += 1
		cartitem.save()
		num_of_item = cart.num_of_items
	return JsonResponse(num_of_item, safe=False)



def cart(request):
	cart = None
	cartitems = []

	if request.user.is_authenticated:
		cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
		cartitems = cart.cart_items.all()

	return render(request, 'cart.html', {'cart':cart, 'cartitems':cartitems})


def contact(request):
	messages.success(request, ('Payments Made Successfully'))
	return render(request, 'contact.html', {})



def confirm_payment(request, pk):
	cart = Cart.objects.get(id=pk)
	cart.completed = True
	cart.save()
	messages.success(request, 'Payments Made Successfully')
	return redirect('/products')

