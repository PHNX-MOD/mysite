from django.contrib import admin
from .models import Product, OrderLine, Order, Contact

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(OrderLine)
admin.site.register(Order)