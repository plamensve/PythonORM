import os

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Product, Category, Customer, Order, OrderProduct
from django.db.models import Count, Sum


def product_quantity_ordered():
    orders = ((OrderProduct.objects.values('product__name')
               .filter(product__is_available=True)
               .annotate(total_quantity=Sum('quantity')))
              .order_by('-total_quantity'))

    print(orders.query)
    result = []

    for o in orders:
        result.append(f"Quantity ordered of {o['product__name']}: {o['total_quantity']}")

    return '\n'.join(result)


def ordered_products_per_customer():
    orders = Order.objects.prefetch_related('orderproduct_set__order')

    result = []

    for order in orders:
        result.append(f"Order ID: {order.id}, Customer: {order.customer.username}")
        for info in order.orderproduct_set.all():
            result.append(f"- Product: {info.product.name}, Category: {info.product.category.name}")

    return '\n'.join(result)


print(ordered_products_per_customer())
