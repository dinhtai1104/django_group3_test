from django import views
from django.http import HttpResponse
from django.shortcuts import render

from ecomerce.models import *


# Create your views here.

def cart(request):
   context = {'number': '100'}
   return render(request, 'store/cart.html', context)


class Home():
   
   def login(request):
      return ""

   def book(request):
      products = Book.objects.all()
      context = {'products': products}
      return render(request, 'store/home.html', context)
   def shoes(request):
      products = Shoes.objects.all()
      context = {'products': products}
      return render(request, 'store/home.html', context)
   def laptop(request):
      products = Laptop.objects.all()
      context = {'products': products}
      return render(request, 'store/home.html', context)
   def electronics(request):
      products = Electronic.objects.all()
      context = {'products': products}
      return render(request, 'store/home.html', context)
   def mobilephones(request):
      products = MobilePhone.objects.all()
      context = {'products': products}
      return render(request, 'store/home.html', context)
   def clothes(request):
      products = Clothes.objects.all()
      context = {'products': products}
      return render(request, 'store/home.html', context)

## Example

# def cart2(req):
#    context={'name_site': 'Shopee', 'other': []}
#    return render(req, 'store/cart.html', context)
# def home2(req):
#    context={'name_site': 'Shopee'}
#    return render(req, 'store/cart.html', context)
# def home3(req):
#    context={'name_site': 'Shopee'}
#    return render(req, 'store/cart.html', context)
