from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact-us"),
    path("tracker/", views.home, name="trackingStatus"),
    path("search/", views.home, name="search"),
    path("list/", views.productsView, name="products"),
    path("checkout", views.home, name="checkout"),  
]
