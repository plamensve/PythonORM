import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Article, Review
from django.db.models import Q, Count, Avg


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


def get_latest_article():
    article = (Article.objects.all()
               .prefetch_related('authors')
               .annotate(
        number_of_reviews=Count('review'),
        avg_rating=Avg('review__rating')
    )
               .order_by('-published_on')
               .first())

    if not article:
        return ''

    article_authors = [a.full_name for a in article.authors.all().order_by('full_name')]

    avg_rating = article.avg_rating if article.number_of_reviews > 0 else 0

    return (f"The latest article is: {article.title}. "
            f"Authors: {', '.join(article_authors)}. "
            f"Reviewed: {article.number_of_reviews} times. "
            f"Average Rating: {avg_rating:.2f}.")


def get_top_rated_article():
    top_article = Article.objects.annotate(
        avg_rating=Avg('review__rating'),
        review_count=Count('review')
    ).order_by('-avg_rating', 'title').first()

    if not top_article or not top_article.review_count:
        return ''

    return (f"The top-rated article is: {top_article.title}, "
            f"with an average rating of {top_article.avg_rating:.2f}, "
            f"reviewed {top_article.review_count} times.")


def ban_author(email=None):
    if email is None:
        return "No authors banned."

    try:
        author = Author.objects.get(email__exact=email)
    except Author.DoesNotExist:
        return 'No authors banned.'

    author.is_banned = True
    author.save()

    review_count = author.review_set.count()
    author.review_set.all().delete()

    return f"Author: {author.full_name} is banned! {review_count} reviews deleted."


print(ban_author('as@dev.com'))
