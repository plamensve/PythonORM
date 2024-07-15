import os
import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import RealEstateListing


# Run the 'by_property_type' method
house_listings = RealEstateListing.objects.by_property_type('House')
print("House listings:")
for listing in house_listings:
    print(f"- {listing.property_type} in {listing.location}")

# Run the 'in_price_range' method
affordable_listings = RealEstateListing.objects.in_price_range(75000.00, 120000.00)
print("Price in range listings:")
for listing in affordable_listings:
    print(f"- {listing.property_type} in {listing.location}")

# Run the 'with_bedrooms' method
two_bedroom_listings = RealEstateListing.objects.with_bedrooms(2)
print("Two-bedroom listings:")
for listing in two_bedroom_listings:
    print(f"- {listing.property_type} in {listing.location}")

# Run the 'popular_locations' method
popular_locations = RealEstateListing.objects.popular_locations()
print("Popular locations:")
for location in popular_locations:
    print(f"- {location['location']}; Listings: {location['location_count']}")
