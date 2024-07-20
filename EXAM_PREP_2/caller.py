import os

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Profile, Product, Order
from django.db.models import Q, Count, F
import random
from decimal import Decimal


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
    try:
        order = Order.objects.prefetch_related('products').latest('creation_date')

        if not order:
            return ''

        product_names = ', '.join(product.name for product in order.products.all().order_by('name'))

        return f"Last sold products: {product_names}"
    except Order.DoesNotExist:
        return ''


def get_top_products():
    top_products = Product.objects.annotate(num_orders=Count('order')) \
                       .filter(num_orders__gt=0) \
                       .order_by('-num_orders', 'name')[:5]

    if top_products:
        top_products_str = "\n".join(f'{product.name}, sold {product.num_orders} times' for product in top_products)
        return f"Top products:\n{top_products_str}"
    return ""

def apply_discounts():
    discounted_orders = Order.objects.annotate(num_products=Count('products')) \
        .filter(num_products__gt=2, is_completed=False) \
        .update(total_price=F('total_price') * 0.9)

    return f'Discount applied to {discounted_orders} orders.'


def complete_order():
    order = Order.objects.filter(is_completed=False).order_by('creation_date').first()
    if order is None:
        return ""

    order.is_completed = True
    order.save()

    for product in order.products.all():
        product.in_stock -= 1

        if product.in_stock == 0:
            product.is_available = False
        product.save()

    return "Order has been completed!"
