from django.shortcuts import render
from .models import Product
from math import ceil

def discountPage(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'store/discount.html', params)


def about(request):
    return render(request, 'store/about.html')

def home(request):
    request.session["categories"] = list(Product.objects.values('category').distinct())
    request.session["sub_categories"] = list(Product.objects.values('sub_category').distinct())
    return render(request, 'store/home.html')

def productDetail(request):
    return render(request, 'store/product_detail.html')

def productList(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'store/product_list.html', context)

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


