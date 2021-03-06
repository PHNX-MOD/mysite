from django.shortcuts import render
from .models import Product, Contact, Category, SubCategory
from math import ceil
from django.views.generic import DetailView, ListView
from datetime import datetime, date, time, timedelta


def about(request):
    return render(request, 'store/about.html')

class Home(ListView):
    model = Category
    template_name = 'store/home.html'
    context_object_name = 'home_list'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.distinct()
        context['products'] = Product.objects.all()
        context['sub_categories'] = SubCategory.objects.distinct()
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
    context_object_name = 'product'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'store/category_detail.html'
    context_object_name = 'category'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.distinct()
        context['sub_categories'] = SubCategory.objects.distinct()
        category = context['category']
        products = Product.objects.filter(category=category)
        context['products'] = products
        return context

class SubCategoryDetail(DetailView):
    model = SubCategory
    template_name = 'store/subcategory_detail.html'
    context_object_name = 'sub_category'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.distinct()
        context['sub_categories'] = SubCategory.objects.distinct()
        sub_category = context['sub_category']
        products = Product.objects.filter(sub_category=sub_category)
        context['products'] = products
        return context

def new_product_Page(request):
    date = datetime.today()
    start_week = date - timedelta(date.weekday())
    end_week = start_week + timedelta(7)
    context = {
        'products': Product.objects.filter(pub_date__range=[start_week, end_week]).order_by('-pub_date'),
        'categories': Category.objects.distinct(),
        'sub_categories': SubCategory.objects.distinct()
    }
    return render(request, 'store/new_product.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'store/contact.html')

def discountPage(request):
    context = {
        'products': Product.objects.all(),
        'categories':Category.objects.distinct(),
        'sub_categories': SubCategory.objects.distinct()
    }
    return render(request, 'store/discount.html', context)

def tracker(request):
    return render(request, 'store/tracker.html' )

def search(request):
    return render(request, 'store/search.html' )

def checkout(request):
    return render(request, 'store/checkout.html')

#not in use
def discountPageNotInUse(request):
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



