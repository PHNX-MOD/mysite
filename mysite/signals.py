from django.contrib.auth.signals import user_logged_in
from store.models import Product

def load_objects(sender, user, request, **kwargs):
    request.session["categories"] = list(Product.objects.values('id', 'category'))

user_logged_in.connect(load_objects)
