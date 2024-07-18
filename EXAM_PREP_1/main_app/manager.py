from django.db import models
from django.db.models import Count


class DirectorManager(models.Manager):
    def get_directors_by_movies_count(self):
        director_objects = self.all().annotate(number_of_movies=Count('director_movies')
                                               ).order_by('-number_of_movies', 'full_name')

        return director_objects
