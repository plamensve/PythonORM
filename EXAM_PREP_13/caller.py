import os
import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import RealEstateListing

# Run the 'popular_locations' method
popular_locations = RealEstateListing.objects.popular_locations()
print("Popular locations:")
for location in popular_locations:
    print(f"- {location['location']}; Listings: {location['location_count']}")

# print(RealEstateListing.objects.popular_locations())
