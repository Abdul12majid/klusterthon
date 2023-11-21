from django.shortcuts import render, redirect
from .models import Product, Category, Cart, CartItem
from django.http import JsonResponse
import json

# Create your views here.
def home(request):
	category_1 = 'New Arrivals'
	category_2 = 'Top sales'
	category_3 = 'Features'
	get_1 = Category.objects.get(name='New Arrivals')
	get_2 = Category.objects.get(name=category_2)
	get_3 = Category.objects.get(name=category_3)
	products = Product.objects.all()
	#print(get_1)
	products_2 = Product.objects.filter(category=get_2)
	products_3 = Product.objects.filter(category=get_3)
	return render(request, 'home.html', {'products':products, 'products_2':products_2, 'products_3':products_3})


'''
def category(request, foo):
	foo = foo.replace('-', ' ')
	try:
		category = Category.objects.get(name=foo)
		products = Product.objects.filter(category=category)
		return render(request, 'commerce/category.html', {'products':products, 'category':category})
	except:
		messages.success(request, ("Category doesn't exist"))
		return redirect('home')
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
	return JsonResponse("it is working", safe=False)