import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# from main_app.models import ZooKeeper, Veterinarian, Mammal
#
# # Keep the data from the previous exercise, so you can reuse it
#
# zookeeper = ZooKeeper.objects.create(first_name="Peter", last_name="Johnson", phone_number="0899524265", specialty="Mammals")
# mammal = Mammal.objects.get(name="Fluffy")
# zookeeper.managed_animals.add(mammal)
# veterinarian = Veterinarian.objects.create(first_name="Dr. Michael", last_name="Smith", phone_number="9876543210", license_number="VET12345")
#
# zookeeper_from_db = ZooKeeper.objects.first()
# print(f"{zookeeper_from_db.first_name} {zookeeper_from_db.last_name} is a ZooKeeper.")
#
# veterinarian_from_db = Veterinarian.objects.first()
# print(f"{veterinarian_from_db.first_name} {veterinarian_from_db.last_name} is a Veterinarian.")


# from main_app.models import ZooDisplayAnimal
#
# is_proxy = ZooDisplayAnimal._meta.proxy
#
# if is_proxy:
#     print("ZooDisplayAnimal is a proxy model.")
# else:
#     print("ZooDisplayAnimal is not a proxy model.")
#
# from main_app.models import ZooKeeper
#
# zookeeper = ZooKeeper(first_name="John", last_name="Doe", phone_number="0123456789", specialty="Birds")
# zookeeper.full_clean()
# zookeeper.save()

# from main_app.models import ZooDisplayAnimal
#
# # Keep the data from the previous exercises, so you can reuse it
#
# all_animals_info = ZooDisplayAnimal.objects.all()
# for a in all_animals_info:
#     print(a.display_info())
#     print(a.is_endangered())
