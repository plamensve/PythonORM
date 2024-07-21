from decimal import Decimal

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Count, Avg


class RealEstateListingManager(models.Manager):
    def by_property_type(self, property_type: str):
        estate_objects = self.filter(property_type=property_type)

        return estate_objects

    def in_price_range(self, min_price: Decimal, max_price: Decimal):
        estate_objects = self.filter(price__gte=min_price, price__lte=max_price)

        return estate_objects

    def with_bedrooms(self, bedrooms_count: int):
        estate_objects = self.filter(bedrooms=bedrooms_count)

        return estate_objects

    def popular_locations(self):
        most_visit_locations = (self.values('location')
                                .annotate(location_count=Count('location'))
                                .order_by('-location_count', 'location'))[:2]

        return most_visit_locations


class VideoGameManager(models.Manager):
    def games_by_genre(self, genre: str):
        return self.filter(genre=genre)

    def recently_released_games(self, year: int):
        return self.filter(release_year__gte=year)

    def highest_rated_game(self):
        return self.all().order_by('-rating').first()

    def lowest_rated_game(self):
        return self.all().order_by('-rating').last()

    def average_rating(self):
        games = self.all().aggregate(avg_rating=Avg('rating'))
        return f"{games['avg_rating']:.1f}"
