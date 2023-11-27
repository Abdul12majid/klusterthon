
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('create_profile', views.create_profile, name='create-profile'),    
    path('login_user', views.login_user, name='login-user'),
    path('logout/', views.logout_user, name='logout'),
    path('login_admin', views.login_admin, name='login-admin'),
    path('tables', views.tables, name='tables'),
]
