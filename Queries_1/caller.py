import os
from datetime import date, timedelta

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Book, Artist, Song, Product, Review, Driver, DrivingLicense


def show_all_authors_with_their_books():
    authors = Author.objects.all()
    result = []

    for author in authors:
        books = author.book_set.all()

        if not books:
            continue

        titles = [book.title for book in books]

        result.append(f"{author.name} has written - {', '.join(titles)}!")
    return '\n'.join(result)


def delete_all_authors_without_books():
    return Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str):
    artist = Artist.objects.get(name=artist_name)
    return artist.songs.all().order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()

    total_rating = sum(r.rating for r in reviews)

    avg_rating = total_rating / len(reviews)
    return avg_rating


def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews():
    return get_products_with_no_reviews().delete()


def calculate_licenses_expiration_dates():
    drivers = Driver.objects.all().order_by('license__issue_date')
    result = []

    for driver in drivers:
        if hasattr(driver, 'license') and driver.license is not None:
            expiration_date = driver.license.issue_date + timedelta(days=365)
            result.append(f"License with number: {driver.license.license_number} expires on {expiration_date}!")

    return '\n'.join(result)


def get_drivers_with_expired_licenses(due_date: date):
    drivers = Driver.objects.all()

    result = []
    for driver in drivers:
        if hasattr(driver, 'license') and driver.license is not None:
            license_expire = driver.license.issue_date + timedelta(days=365)

            if license_expire > due_date:
                result.append(driver)
    return result

























