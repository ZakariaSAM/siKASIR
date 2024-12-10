from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('kasir/', views.kasir, name='kasir'),
    path('gudang/', views.gudang, name='gudang'),
    path('pembukuan/', views.pembukuan, name='pembukuan'),
    path('inputdata/', views.inputdata, name='inputdata'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]

