import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Profile, Product, Order
from django.db.models import Q, Count, F


def get_profiles(search_string=None):
    if search_string is None:
        return ''

    profiles = (Profile.objects.filter(
        Q(full_name__icontains=search_string) |
        Q(email__icontains=search_string) |
        Q(phone_number__icontains=search_string)).annotate(nums_of_order=Count('order'))
                .order_by('full_name'))

    if not profiles:
        return ''

    result = []
    for profile in profiles:
        result.append(f"Profile: {profile.full_name}, "
                      f"email: {profile.email}, "
                      f"phone number: {profile.phone_number}, "
                      f"orders: {profile.nums_of_order}")

    return '\n'.join(result)


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()

    if not profiles:
        return ''

    result = []

    for profile in profiles:
        result.append(f"Profile: {profile.full_name}, orders: {profile.number_of_orders}")

    return '\n'.join(result)


def get_last_sold_products():
    try:
        order = Order.objects.all().latest('creation_date')
    except Order.DoesNotExist:
        return ''

    products = order.products.all().order_by('name')
    if not products.exists():
        return ''

    product_names = [p.name for p in products]
    return f"Last sold products: {', '.join(product_names)}"


def get_top_products():
    top_products = Product.objects.annotate(num_orders=Count('order')) \
                       .filter(num_orders__gt=0) \
                       .order_by('-num_orders', 'name')[:5]

    if top_products:
        top_products_str = "\n".join(f'{product.name}, sold {product.num_orders} times' for product in top_products)
        return f"Top products:\n{top_products_str}"
    return ""


def apply_discounts():
    orders = Order.objects.annotate(num_products=Count('products')).filter(num_products__gt=2, is_completed=False)

    num_of_updated_orders = orders.update(total_price=F('total_price') * 0.9)

    return f"Discount applied to {num_of_updated_orders} orders."


def complete_order():
    order = Order.objects.all().filter(is_completed=False).first()
    if order is None:
        return ''

    order.is_completed = True
    order.save()

    for product in order.products.all():
        if product.in_stock > 0:
            product.in_stock -= 1

        if product.in_stock == 0:
            product.is_available = False

        product.save()

    return "Order has been completed!"





















