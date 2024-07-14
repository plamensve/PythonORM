import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db import connection
from django.db.models import Sum
from pprint import pprint
from main_app.models import Product, Order, OrderProduct


def product_quantity_ordered():
    total_product_ordered = Product.objects.annotate(
        total_order_quantity=Sum('orderproduct__quantity')
    ).exclude(total_order_quantity=None).order_by('-total_order_quantity')

    result = []
    for product in total_product_ordered:
        result.append(f"Quantity ordered of {product.name}: {product.total_order_quantity}")
    return '\n'.join(result)


def ordered_products_per_customer():
    result = []

    for x in Order.objects.all():
        result.append(f"Order ID: {x.pk}, Customer: {x.customer.username}")
        for o in OrderProduct.objects.filter(order__pk=x.id):
            result.append(f"- Product: {o.product.name}, Category: {o.product.category.name}")
    return '\n'.join(result)

# print(ordered_products_per_customer())
# pprint(connection.queries)






















