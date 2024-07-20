import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Book, Artist, Song, Product, Review


def show_all_authors_with_their_books():
    authors = Author.objects.all()
    result = []

    for a in authors:
        books = ', '.join(b.title for b in a.book_set.all())

        if not books:
            continue

        result.append(f"{a.name} has written - {books}!")

    return '\n'.join(result)


def delete_all_authors_without_books():
    authors = Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str):
    artist = Artist.objects.get(name=artist_name)

    return artist.songs.all().order_by('-title')


def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.get(name=product_name)
    cumulative_rating = 0

    for review in product.reviews.all():
        cumulative_rating += review.rating

    return cumulative_rating / len(product.reviews.all())


def get_reviews_with_high_ratings(threshold: int):
    reviews = Review.objects.filter(rating__gte=threshold)

    return reviews


def get_products_with_no_reviews():
    products_without_reviews = Product.objects.filter(reviews__rating__isnull=True).order_by('-name')

    return products_without_reviews


def delete_products_without_reviews():
    products_without_reviews = Product.objects.filter(reviews__rating__isnull=True).delete()


