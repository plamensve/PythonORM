import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Profile, Product, Order
from django.db.models import Q, Count


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

