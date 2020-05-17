from django.contrib import admin
from .models import Product, OrderLine, Order, Contact, Category, SubCategory

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(OrderLine)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(SubCategory)