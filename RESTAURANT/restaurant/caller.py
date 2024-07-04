import os
from datetime import datetime

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurant.settings")
django.setup()

from main_app.models import Client, Menu, Order


# client1 = Client.objects.create(first_name='Plamen', last_name='Svetoslavov')
# client2 = Client.objects.create(first_name='Anton', last_name='Jordanov')
# client3 = Client.objects.create(first_name='Nataliya', last_name='Kamenova')
# client4 = Client.objects.create(first_name='Ivana', last_name='Rusinova')
# client5 = Client.objects.create(first_name='Kameliya', last_name='Todorova')
#
# menu1 = Menu.objects.create(name='Pasta', price=15.50)
# menu2 = Menu.objects.create(name='Burger', price=10.00)
# menu3 = Menu.objects.create(name='Spageti', price=9.00)
# menu4 = Menu.objects.create(name='Cake', price=19.00)
# menu5 = Menu.objects.create(name='Beef', price=29.00)


def make_an_order(first_name, last_name, product):
    client = Client.objects.filter(first_name=first_name, last_name=last_name)
    menu = Menu.objects.filter(name=product)

    order = []

    for c in client:
        order.append(c.id)

    for m in menu:
        order.append(m.id)

    client_order = Order.objects.create(date_time=datetime.now(), client_id=order[0], menu_id=order[1])


def order_information(client_order_id):
    order_info = Order.objects.filter(client_id=client_order_id)

    client_meal_info = []

    for i in order_info:
        result = (i.client_id, i.menu_id)
        client_meal_info.append(result)

    msg = []
    for x in client_meal_info:
        client = Client.objects.filter(id=x[0])
        meal = Menu.objects.filter(id=x[1])

        for c in client:
            for m in meal:
                msg.append(f"Order by {c.first_name} {c.last_name} for {m.name}")

    return '\n'.join(msg)


# make_an_order('Anton', 'Jordanov', 'Pasta')
print(order_information(9))
# delete_order(8, 7)
