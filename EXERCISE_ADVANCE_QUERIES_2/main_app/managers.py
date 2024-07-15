from decimal import Decimal

from django.db import models
from django.db.models import Count, Max, Min, Avg


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


class VideoGameManager(models.Manager):
    def games_by_genre(self, genre: str):
        game_object = self.filter(genre=genre)

        return game_object

    def recently_released_games(self, year: int):
        game_object = self.filter(release_year__gte=year)

        return game_object

    def highest_rated_game(self):
        game_object = self.aggregate(Max('rating'))

        return self.get(rating=game_object['rating__max'])

    def lowest_rated_game(self):
        game_object = self.aggregate(Min('rating'))

        return self.get(rating=game_object['rating__min'])

    def average_rating(self):
        game_object = self.aggregate(Avg('rating'))

        return f"{game_object['rating__avg']:.1f}"







































































