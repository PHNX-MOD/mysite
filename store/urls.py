from django.urls import path
from . import views
from .views import ProductDetail, CategoryDetail

urlpatterns = [
    path("", views.home, name="home"),
    path("discount/", views.discountPage, name="discount"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact-us"),
    path("tracker/", views.home, name="trackingStatus"),
    path("search/", views.home, name="search"),
    path("list/", views.productsView, name="products"),
    path("product_detail/<int:pk>", ProductDetail.as_view(), name="product_detail"),
    path("category-detail/<int:pk>", CategoryDetail.as_view(), name="category_detail"),
    path("checkout", views.home, name="checkout"),
]
