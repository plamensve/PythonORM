import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Person, Item, Order

result = Order.objects.all()
for i in result:
    print(i.status)