import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db import connection
from django.db.models import Sum, Q, F
from pprint import pprint
from main_app.models import Product, Order, OrderProduct


def product_quantity_ordered():
    orders = Product.objects.annotate(
        total=Sum('orderproduct__quantity')
    ).values('name', 'total').order_by('-total')

    result = []
    for order in orders:
        if order['total']:
            result.append(f"Quantity ordered of {order['name']}: {order['total']}")
    return '\n'.join(result)


def ordered_products_per_customer():
    result = []

    # for x in Order.objects.all():
    #     result.append(f"Order ID: {x.pk}, Customer: {x.customer.username}")
    #     for o in OrderProduct.objects.filter(order__pk=x.id):
    #         result.append(f"- Product: {o.product.name}, Category: {o.product.category.name}")
    # return '\n'.join(result)

    orders = Order.objects.prefetch_related('orderproduct_set__product__category').order_by('id')
    for order in orders:
        result.append(f"Order ID: {order.pk}, Customer: {order.customer.username}")
        for o in order.orderproduct_set.all():
            result.append(f"- Product: {o.product.name}, Category: {o.product.category.name}")
    return '\n'.join(result)


def filter_products():
    products = Product.objects.filter(is_available=True).order_by('-price', 'name')
    result = []
    for product in products:
        if product.price > 3.00:
            result.append(f"{product.name}: {product.price}lv.")

    return '\n'.join(result)


def give_discount():
    products = Product.objects.filter(
        Q(is_available=True) & Q(price__gt=3.00)
        ).update(price=F('price') * 0.7)

    result = []

    discounted_products = Product.objects.filter(is_available=True).order_by('-price', 'name')
    for p in discounted_products:
        result.append(f"{p.name}: {p.price}lv.")

    return '\n'.join(result)

print(give_discount())

    # result = []
    #
    # for product in products:
    #     if product.price > 3.00:
    #         product.price = float(product.price) * 0.7
    #     result.append((product.name, product.price))
    #
    # result_sorted = sorted(result, key=lambda x: -x[1])
    #
    # result_formatted = [f"{name}: {price:.2f}lv." for name, price in result_sorted]
    #
    # return '\n'.join(result_formatted)



