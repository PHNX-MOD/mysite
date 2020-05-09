from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
from django.http import JsonResponse
from .contexting import list_of_categories, list_of_sub_categories

def home(request):
    
    """
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
      prod = Product.objects.filter(category = cat)
      n = len(prod)
      nSlides = n//4 + ceil((n/4)-(n//4))
      allProds.append([prod,range(1, nSlides), nSlides])
    params = {'allProds': allProds,
              "categories_list": list_of_categories(),
              "sub_categories_list": list_of_sub_categories()
              }
    """
    request.session["categories"] = list(Product.objects.values('id', 'category'))
    return render(request, 'store/home.html')

def about(request, *args, **kwargs):
    context = {"categories_list": list_of_categories(),
               "sub_categories_list":list_of_sub_categories()}
    return render(request, 'store/about.html', context)



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


