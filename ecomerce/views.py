from django import views
from django.http import HttpResponse
from django.shortcuts import render

from ecomerce.models import Product


# Create your views here.
def home(request):
   products = Product.objects.all()
   context = {'products': products}
   return render(request, 'store/home.html', context)

def cart(request):
   context = {'number': '100'}
   return render(request, 'store/cart.html', context)


class Home():
   
   def login(request):
      return ""

   def home(request):
      products = Product.objects.all()
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
