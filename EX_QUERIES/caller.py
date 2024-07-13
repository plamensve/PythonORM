import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Book, Artist, Song


def show_all_authors_with_their_books():
    result = []

    authors = Author.objects.all().order_by('id')
    for author in authors:
        books = author.book_set.all()

        if not books:
            continue

        titles = [b.title for b in books]
        result.append(f"{author.name} has written - {', '.join(titles)}!")

    return '\n'.join(result)


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str):
    artist = Artist.objects.get(name=artist_name).songs.all().order_by('-id')
    return artist


def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)
