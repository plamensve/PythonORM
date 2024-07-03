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


def delete_order(client_id, menu_id):
    order = Order.objects.filter(client_id=client_id).filter(menu_id=menu_id).delete()


def order_information(client_order_id):
    order_info = Order.objects.all()

    order_list_info = []
    for i in order_info:
        if i.client_id == client_order_id:
            order_list_info.append(i.client_id)
            order_list_info.append(i.menu_id)

    client = Client.objects.filter(id=order_list_info[0])
    product = Menu.objects.filter(id=order_list_info[1])
    order_list_info.clear()

    result = []

    for c in client:
        result.append(c.first_name)
        result.append(c.last_name)

    for p in product:
        result.append(p.name)
        result.append(p.price)

    return result


# make_an_order('Kameliya', 'Todorova', 'Beef')
# print(order_information(8))
# delete_order(8, 7)