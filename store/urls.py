from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("discount/", views.discountPage, name="discount"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact-us"),
    path("tracker/", views.home, name="trackingStatus"),
    path("search/", views.home, name="search"),
    path("list/", views.productsView, name="products"),
    path("product-detail/", views.productDetail, name="product_detail"),
    path("product-list/", views.productList, name="product_list"),
    path("checkout", views.home, name="checkout"),  
]
