
from django.urls import path
from . import views

urlpatterns = [
    path('', views.docs, name='docs'),
    path('home', views.home, name='home-home'),
    path('add_to_cart', views.add_to_cart, name='add'),
    path('cart', views.cart, name='add-cart'),
    path('contact', views.contact, name='contact'),

    path('confirm_payment/<str:pk>', views.confirm_payment, name='payment'),
    
]
