from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

def home(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    return render(request, 'store/home.html', params)

def about(request):
  return render(request, 'store/about.html' )

def contact(request):
  return render(request, 'store/contact.html' )

def productsView(request):
  return render(request, 'store/products.html' )

def tracker(request):
  return render(request, 'store/tracker.html' )

def search(request):
  return render(request, 'store/search.html' )

def checkout(request):
  return render(request, 'store/checkout.html' )