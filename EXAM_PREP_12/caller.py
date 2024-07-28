import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Product, Category, Customer, Order, OrderProduct
from django.db.models import Count, F
from django.db.models import Sum


def product_quantity_ordered():
    # Aggregate the total quantity ordered for each product
    product_quantities = OrderProduct.objects.values('product__name').annotate(
        total_quantity=Sum('quantity')
    ).filter(total_quantity__gt=0).order_by('-total_quantity')

    print(product_quantities)
    # Format the output as requested
    result = "\n".join([
        f"Quantity ordered of {item['product__name']}: {item['total_quantity']}"
        for item in product_quantities
    ])


def ordered_products_per_customer():
    orders = Order.objects.all().prefetch_related('products')

    result = []
    for order in orders:
        result.append(f"Order ID: {order.id}, Customer: {order.customer.username}")
        for product in order.products.all():
            result.append(f"- Product: {product.name}, Category: {product.category.name}")

    return '\n'.join(result)


def filter_products():
    products = Product.objects.all().filter(is_available=True, price__gt=3.00).order_by('-price')

    result = []
    for p in products:
        result.append(f"{p.name}: {p.price}lv.")

    return '\n'.join(result)

def give_discount():
    products_for_discount = (Product.objects.all()
                             .filter(is_available=True, price__gt=3.00)
                             .update(price=F('price') * 0.7))

    all_products = Product.objects.all().filter(is_available=True).order_by('-price', 'name')

    result = []

    for p in all_products:
        result.append(f"{p.name}: {p.price}lv.")

    return '\n'.join(result)

