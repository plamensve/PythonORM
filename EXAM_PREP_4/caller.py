import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Product, Category, Customer, Order, OrderProduct
from django.db.models import Count, Sum

from django.db.models import Sum


from django.db.models import Sum

def product_quantity_ordered():
    orders = (OrderProduct.objects.values('product__name').filter(product__is_available=True)
              .annotate(total_quantity=Sum('quantity'))).order_by('-total_quantity')

    result = []

    for o in orders:
        result.append(f"Quantity ordered of {o['product__name']}: {o['total_quantity']}")

    return '\n'.join(result)


# print(product_quantity_ordered())

