import os
import django
from unicodedata import decimal

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db import models
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom


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


def show_all_locations():
    result = []
    for i in Location.objects.all().order_by('-id'):
        result.append(f"{i.name} has a population of {i.population}!")

    return '\n'.join(result)


def new_capital():
    location = list(Location.objects.all())
    location = location[0]
    location.is_capital = True
    location.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location():
    location = list(Location.objects.all())
    location = location[0]
    location.delete()


# print(show_all_locations())
# print(new_capital())
# print(get_capitals())


def apply_discount():
    cars = Car.objects.all()

    # for c in car:
    #     discount = 0
    #     for n in str(c.year):
    #         discount += int(n)
    #     discounted_price = float(c.price) - (discount / 100) * float(c.price)
    #     c.price_with_discount = discounted_price
    #     c.save()

    for c in cars:
        discount_off = sum(int(d) for d in str(c.year)) / 100
        money_discount = float(c.price) * discount_off
        c.price_with_discount = float(c.price) - money_discount
        c.save()


# apply_discount()

def get_recent_cars():
    return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')


def delete_last_car():
    Car.objects.last().delete()


def show_unfinished_tasks():
    task = Task.objects.all().filter(is_finished=False)
    return '\n'.join(str(t) for t in task)


# print(show_unfinished_tasks())

def complete_odd_tasks():
    task = Task.objects.all()
    for t in task:
        if t.id % 2 == 1:
            t.is_finished = True
            t.save()


# complete_odd_tasks()

def encode_and_replace(text: str, task_title: str):
    decoded_text = ''.join(chr(ord(symbol) - 3) for symbol in text)
    Task.objects.filter(title=task_title).update(description=decoded_text)

    # task = Task.objects.all()
    #
    # encoded = text
    # decoded = [chr(ord(i) - 3) for i in encoded]
    # for t in task:
    #     if t.title == task_title:
    #         t.description = ''.join(decoded)
    #     t.save()


# encode_and_replace("Zdvk#wkh#glvkhv$", "Simple Task")
# print(Task.objects.get(title='Simple Task').description)


def get_deluxe_rooms():
    rooms = HotelRoom.objects.all().filter(room_type='Deluxe')
    even_deluxe_rooms = [str(r) for r in rooms if r.id % 2 == 0]

    return "\n".join(even_deluxe_rooms)


# print(get_deluxe_rooms())

def increase_room_capacity():
    rooms = HotelRoom.objects.all().order_by('id')

    previous_room_capacity = None

    for room in rooms:
        if not room.is_reserved:
            continue

        if previous_room_capacity is not None:
            room.capacity += previous_room_capacity
        else:
            room.capacity = room.capacity + room.id

        previous_room_capacity = room.capacity
        room.save()


def reserve_first_room():
    room = HotelRoom.objects.first()
    room.is_reserved = True
    room.save()


def delete_last_room():
    room = HotelRoom.objects.last()
    if not room.is_reserved:
        room.delete()
