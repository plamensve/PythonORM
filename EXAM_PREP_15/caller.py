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

