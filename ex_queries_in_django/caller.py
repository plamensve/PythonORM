import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery


def show_highest_rated_art():
    highest_rating = 0
    name = None
    id_num = 0

    artist = ArtworkGallery.objects.all()
    for a in artist:
        if a.rating > highest_rating:
            highest_rating = a.rating
            name = a.art_name
            id_num = a.id

        elif a.rating == highest_rating and a.id < id_num:
            highest_rating = a.rating
            name = a.art_name
            id_num = a.id
        else:
            continue

    return f"{name} is the highest-rated art with a {highest_rating} rating!"


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery):
    artworks = [first_art, second_art]
    ArtworkGallery.objects.bulk_create(artworks)


def delete_negative_rated_arts():
    arts = ArtworkGallery.objects.filter(rating__lt=0)
    arts.delete()


artwork1 = ArtworkGallery(artist_name='Vincent van Gogh', art_name='Starry Night', rating=4, price=1200000.0)
artwork2 = ArtworkGallery(artist_name='Leonardo da Vinci', art_name='Mona Lisa', rating=5, price=1500000.0)

# # Bulk saves the instances
# bulk_create_arts(artwork1, artwork2)
# print(show_highest_rated_art())
# print(ArtworkGallery.objects.all())
