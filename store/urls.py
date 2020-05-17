from django.urls import path
from . import views
from .views import ProductDetail, CategoryDetail, Home, SubCategoryDetail


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("discount/", views.discountPage, name="discount"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    #path("tracker/", views.home, name="trackingStatus"),
    #path("search/", views.home, name="search"),
    path("product_detail/<int:pk>", ProductDetail.as_view(), name="product_detail"),
    path("category_detail/<int:pk>", CategoryDetail.as_view(), name="category_detail"),
    path("subcategory_detail/<int:pk>", SubCategoryDetail.as_view(), name="subcategory_detail"),
    #path("checkout", views.home, name="checkout"),
    path("new_product/", views.new_product_Page, name="new_product"),
]
