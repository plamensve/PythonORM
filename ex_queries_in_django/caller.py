import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop


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


# artwork1 = ArtworkGallery(artist_name='Vincent van Gogh', art_name='Starry Night', rating=4, price=1200000.0)
# artwork2 = ArtworkGallery(artist_name='Leonardo da Vinci', art_name='Mona Lisa', rating=5, price=1500000.0)


# # Bulk saves the instances
# bulk_create_arts(artwork1, artwork2)
# print(show_highest_rated_art())
# print(ArtworkGallery.objects.all())


def show_the_most_expensive_laptop():
    laptop = Laptop.objects.order_by('-price', '-id').first()
    return f"{laptop.brand} is the most expensive laptop available for {laptop.price}$!"


def bulk_create_laptops(*args):
    Laptop.objects.bulk_create(*args)


def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=['Asus', 'Lenovo']).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=['Apple', 'Dell', 'Acer']).update(memory=16)


def update_operation_systems():
    Laptop.objects.filter(brand__exact='Apple').update(operation_system='MacOS')
    Laptop.objects.filter(brand__exact='Asus').update(operation_system='Windows')
    Laptop.objects.filter(brand__exact='Lenovo').update(operation_system='Chrome OS')
    Laptop.objects.filter(brand__in=['Dell', 'Acer']).update(operation_system='Linux')


def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()



# laptop1 = Laptop(
#     brand='Asus',
#     processor='Intel Core i5',
#     memory=8,
#     storage=256,
#     operation_system='MacOS',
#     price=899.99
# )
# laptop2 = Laptop(
#     brand='Apple',
#     processor='Chrome OS',
#     memory=16,
#     storage=256,
#     operation_system='MacOS',
#     price=1399.99
# )
# laptop3 = Laptop(
#     brand='Lenovo',
#     processor='AMD Ryzen 7',
#     memory=12,
#     storage=256,
#     operation_system='Linux',
#     price=999.99,
# )

# # Create a list of instances
# laptops_to_create = [laptop1, laptop2, laptop3]
#
# # Use bulk_create to save the instances
# bulk_create_laptops(laptops_to_create)
#
# update_to_512_GB_storage()
# update_operation_systems()
#
# # Retrieve 2 laptops from the database
# asus_laptop = Laptop.objects.filter(brand__exact='Asus').get()
# lenovo_laptop = Laptop.objects.filter(brand__exact='Lenovo').get()
#
# print(asus_laptop.storage)
# print(lenovo_laptop.operation_system)
#
# print(show_the_most_expensive_laptop())















