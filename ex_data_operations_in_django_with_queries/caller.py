import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db import models
from main_app.models import Pet


def create_pet(name: str, species: str):
    pet = Pet(
        name=name,
        species=species
    )
    pet.save()
    result = []

    for p in Pet.objects.all():
        result.append(f"{p.name} is a very cute {p.species}!")

    return '\n'.join(result)

# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))
