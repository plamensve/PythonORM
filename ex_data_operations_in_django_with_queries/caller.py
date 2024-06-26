import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db import models
from main_app.models import Pet, Artifact


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


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    artifact = Artifact(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )
    artifact.save()

    return f"The artifact {artifact.name} is {artifact.age} years old!"


def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.is_magical is True and artifact.age > 250:
        artifact.name = new_name
    artifact.save()


def delete_all_artifacts():
    artifact = Artifact.objects.all()

    for a in artifact:
        a.delete()

# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
# artifact_object = Artifact.objects.get(name='Ancient Sword')
# rename_artifact(artifact_object, 'Ancient Shield')
# print(artifact_object.name)