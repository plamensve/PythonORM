import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Article, Review
from django.db.models import Count, Avg


def get_authors(search_name=None, search_email=None):
    if search_name is None and search_email is None:
        return ''

    if search_name and search_email:
        authors = (Author.objects.filter(full_name__icontains=search_name, email__icontains=search_email)
                   .order_by('-full_name'))
    elif search_name:
        authors = (Author.objects.filter(full_name__icontains=search_name)
                   .order_by('-full_name'))
    elif search_email:
        authors = (Author.objects.filter(email__icontains=search_email)
                   .order_by('-full_name'))

    result = []
    for a in authors:
        result.append(f"Author: {a.full_name}, email: {a.email}, status: {'Banned' if a.is_banned else 'Not Banned'}")

    return '\n'.join(result)


def get_top_publisher():
    author = ((Author.objects.annotate(num_of_articles=Count('article'))
               .order_by('-num_of_articles', 'email'))
              .first())

    if not author or not author.num_of_articles:
        return ''

    return f"Top Author: {author.full_name} with {author.num_of_articles} published articles."


def get_top_reviewer():
    author = ((Author.objects.annotate(num_of_articles=Count('review'))
               .order_by('-num_of_articles', 'email'))
              .first())

    if not author or not author.num_of_articles:
        return ''

    return f"Top Reviewer: {author.full_name} with {author.num_of_articles} published reviews."


def get_latest_article():
    article = (Article.objects.prefetch_related('authors')
               .annotate(num_of_reviews=Count('review'), avg_rating=Avg('review__rating'))
               .order_by('-published_on')
               .first())

    if not article:
        return ''

    avg_rating = article.avg_rating if article.num_of_reviews > 0 else 0
    article_authors = [a.full_name for a in article.authors.all().order_by('full_name')]

    result = (f"The latest article is: {article.title}. "
              f"Authors: {', '.join(article_authors)}. "
              f"Reviewed: {article.num_of_reviews} times. "
              f"Average Rating: {avg_rating:.2f}.")

    return result


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

    num_of_reviews = author.review_set.count()
    author.review_set.all().delete()

    result = f"Author: {author.full_name} is banned! {num_of_reviews} reviews deleted."
    return result

print(ban_author('as@dev.com'))







































