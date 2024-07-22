from django.db import models
from django.db.models import Count


class AuthorManager(models.Manager):
    def get_authors_by_article_count(self):
        authors = (self.all()
                   .annotate(number_of_articles=Count('article'))
                   .order_by('-number_of_articles', 'email'))
        return authors
