from django.urls import path 
from . import views


urlpatterns = [
    path('cart/', views.cart),
    path('', views.Home.book),
    path('laptop/', views.Home.laptop),
    path('mobile/', views.Home.mobilephones),
    path('shoes/', views.Home.shoes),
    path('clothes/', views.Home.clothes),
    path('electronics/', views.Home.electronics),
]