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


