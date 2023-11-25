from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from hackathon.models import Cart, Cart_Info
from django.contrib import messages


# Create your views here.
def home(request):
	get_users = User.objects.all()
	item = Cart.objects.all()
	cart_info_ = Cart_Info.objects.all()
	print(item)
	user_count = User.objects.count()
	cart_info = Cart_Info.objects.filter(payment_status=False)
	x = cart_info.count()

	return render(request, 'index.html', {'get_users':get_users, 'user_count':user_count, 'x':x, 'cart_info_':cart_info_})


def login_user(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = User.objects.filter(email=email).exists()
		print(user)
		if user is True:
			get_user = User.objects.get(email=email)
			username = get_user.username

			#if not user.check_password():
			#	messages.success(request, ('wrong password'))
			#	return redirect(request.META.get("HTTP_REFERER"))
			
			user_ = authenticate(request, username=username, password=password)
			if user_ is not None:
				login(request, user_)
				return redirect('/')
			else:
				messages.success(request, ('invalid details'))
				return redirect(request.META.get("HTTP_REFERER"))
		else:
			return redirect('/owner/create_profile')
	return render(request, 'login.html', {})


def create_profile(request):
	if request.method == 'POST':
		
		first_name = request.POST['first_name']
		username = first_name
		last_name = request.POST['last_name']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		if password1==password2:
			if User.objects.filter(username=username).exists():
				a = User.objects.filter(username=username).first()
				return render(request, 'register.html', {'first_name':first_name, 'username':username, 'last_name':last_name, 'email':email, 'a':a})
			elif User.objects.filter(email=email).exists():
				b = User.objects.filter(email=email).exists()
				return render(request, 'register.html', {'first_name':first_name, 'username':username, 'last_name':last_name, 'email':email, 'b':b})
			else:
				user = User.objects.create_user(first_name=first_name, username=username, last_name=last_name, email=email, password=password2)
				user.save()
				login(request, user)
				return redirect('/')
		else:
			c = password1==password2
			return render(request, 'register.html', {'first_name':first_name, 'username':username, 'last_name':last_name, 'email':email, 'c':c})
	return render(request, 'register.html', {})

	
def login_admin(request):
	return render(request, 'login_admin.html', {})

def tables(request):
	get_users = User.objects.all()
	item = Cart.objects.all()
	cart_info = Cart_Info.objects.all()
	print(item)
	return render(request, 'tables.html', {'get_users':get_users, 'cart_info':cart_info})


def logout_user(request):
	logout(request)
	#messages.success(request, (f'You are logged out'))
	return redirect('login-user')











