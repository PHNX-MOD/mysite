from .models import Product

def list_of_categories():
    my_data = list(Product.objects.values("category"))
    refined_new_data = [i['category'] for i in my_data ]
    set_of_refined_new_data = set(refined_new_data)
    list_of_category = list(set_of_refined_new_data)
    return list_of_category

def list_of_sub_categories():
    my_data = list(Product.objects.values("sub_category"))
    refined_new_data = [i['sub_category'] for i in my_data ]
    set_of_refined_new_data = set(refined_new_data)
    list_of_sub_category = list(set_of_refined_new_data)
    return list_of_sub_category

