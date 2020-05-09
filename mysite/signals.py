from django.contrib.auth.signals import user_logged_in

def load_objects(sender, user, request, **kwargs):
    print("Load object into session here!")

user_logged_in.connect(load_objects)