from decimal import Decimal

from django.db import models
from django.db.models import Count, Avg


class RealEstateListingManager(models.Manager):
    def by_property_type(self, property_type: str):
        return self.filter(property_type=property_type)

    def in_price_range(self, min_price: Decimal, max_price: Decimal):
        return self.filter(price__gte=min_price, price__lte=max_price)

    def with_bedrooms(self, bedrooms_count: int):
        return self.filter(bedrooms__exact=bedrooms_count)

    def popular_locations(self):
        locations = self.all().values('location').annotate(location_count=Count('location')
                                                           ).order_by('-location_count', 'location')[:2]
        return locations


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
        avg_rating = self.all().aggregate(avg_rating=Avg('rating'))

        return f"{avg_rating['avg_rating']:.1f}"
















