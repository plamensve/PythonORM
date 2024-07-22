import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Article, Review
from django.db.models import Q, Count


def get_authors(search_name=None, search_email=None):
    if search_name and search_email:
        query = Q(full_name__icontains=search_name) & Q(email__icontains=search_email)
    elif search_name:
        query = Q(full_name__icontains=search_name)
    elif search_email:
        query = Q(email__icontains=search_email)
    else:
        return ''

    authors = Author.objects.filter(query).order_by('-full_name')

    if not authors.exists():
        return ''

    result = []
    for author in authors:
        result.append(f"Author: {author.full_name}, "
                      f"email: {author.email}, "
                      f"status: {'Banned' if author.is_banned else 'Not Banned'}")

    return '\n'.join(result)


def get_top_publisher():
    author = (Author.objects.annotate(number_of_articles=Count('article'))
              .order_by('-number_of_articles', 'email')
              .first())

    if author is None or author.number_of_articles == 0:
        return ''

    return f"Top Author: {author.full_name} with {author.number_of_articles} published articles."


def get_top_reviewer():
    author = (Author.objects.annotate(number_of_reviews=Count('review'))
              .order_by('-number_of_reviews', 'email')
              .first())

    if author is None or author.number_of_reviews == 0:
        return ''

    return f"Top Reviewer: {author.full_name} with {author.number_of_reviews} published reviews."
