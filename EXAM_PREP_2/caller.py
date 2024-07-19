import os

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Profile, Product, Order
from django.db.models import Q, Count
import random


def get_profiles(search_string=None):
    if search_string is None:
        return ''

    profiles = Profile.objects.annotate(num_of_orders=Count('order')).filter(
        Q(full_name__icontains=search_string) |
        Q(email__icontains=search_string) |
        Q(phone_number__icontains=search_string)).order_by('full_name')

    if not profiles:
        return ''

    result = []
    for p in profiles:
        result.append(f"Profile: {p.full_name}, "
                      f"email: {p.email}, "
                      f"phone number: {p.phone_number}, "
                      f"orders: {p.num_of_orders}")

    return '\n'.join(result)


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()

    result = []
    for p in profiles:
        result.append(f"Profile: {p.full_name}, orders: {p.orders_count}")

    return '\n'.join(result)


def get_last_sold_products():
    order = Order.objects.prefetch_related('products').latest('creation_date')

    if not order:
        return ''

    product_names = ', '.join(product.name for product in order.products.all().order_by('name'))

    return f"Last sold products: {product_names}"


print(get_last_sold_products())
