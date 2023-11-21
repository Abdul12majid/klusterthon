
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_to_cart', views.add_to_cart, name='add'),
    
]
