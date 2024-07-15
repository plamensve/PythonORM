from decimal import Decimal

from django.db import models
from django.db.models import Count


class RealEstateListingManager(models.Manager):

    def by_property_type(self, property_type: str):
        property_object = self.filter(property_type=property_type)

        return property_object

    def in_price_range(self, min_price: Decimal, max_price: Decimal):
        property_object = self.filter(price__range=(min_price, max_price))

        return property_object

    def with_bedrooms(self, bedrooms_count: int):
        property_object = self.filter(bedrooms=bedrooms_count)

        return property_object

    def popular_locations(self):
        property_object = self.values('location').annotate(
            location_count=Count('location')
        ).order_by('-location_count', 'location')[:2]

        return property_object









