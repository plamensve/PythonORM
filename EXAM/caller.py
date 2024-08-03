import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Astronaut, Spacecraft, Mission
from datetime import date
from django.db.models import Q, Count, Avg
from django.db import transaction


def get_astronauts(search_string=None):
    if search_string is None:
        return ''

    astronauts = (Astronaut.objects.filter(
        Q(name__icontains=search_string) |
        Q(phone_number__icontains=search_string))
                  .order_by('name'))

    result = []
    for a in astronauts:
        result.append(f"Astronaut: {a.name}, "
                      f"phone number: {a.phone_number}, "
                      f"status: {'Active' if a.is_active else 'Inactive'}")

    return '\n'.join(result)


def get_top_astronaut():
    astronaut = (((Astronaut.objects.all()
                   .annotate(num_of_missions=Count('mission_astronauts')))
                  .order_by('-num_of_missions', 'phone_number'))
                 .first())

    if not astronaut or astronaut.num_of_missions == 0:
        return 'No data.'

    return f"Top Astronaut: {astronaut.name} with {astronaut.num_of_missions} missions."


def get_top_commander():
    astronaut = (((Astronaut.objects.all()
                   .annotate(num_of_missions=Count('mission_commander')))
                  .order_by('-num_of_missions', 'phone_number'))
                 .first())

    if not astronaut or astronaut.num_of_missions == 0:
        return 'No data.'

    return f"Top Commander: {astronaut.name} with {astronaut.num_of_missions} commanded missions."


def get_last_completed_mission():
    try:
        mission = Mission.objects.filter(status='Completed').latest('launch_date')
    except Mission.DoesNotExist:
        return "No data."

    commander_name = mission.commander.name if mission.commander else "TBA"

    astronauts = mission.astronauts.all().order_by('name')
    astronauts_names = ', '.join(a.name for a in astronauts)

    total_spacewalks = sum(a.spacewalks for a in astronauts)

    result = (f"The last completed mission is: {mission.name}. "
              f"Commander: {commander_name}. "
              f"Astronauts: {astronauts_names}. "
              f"Spacecraft: {mission.spacecraft.name}. "
              f"Total spacewalks: {total_spacewalks}.")

    return result


def get_most_used_spacecraft():
    spacecraft = (Spacecraft.objects
                  .annotate(num_missions=Count('mission'))
                  .order_by('-num_missions', 'name')
                  .first())

    if not spacecraft or spacecraft.num_missions == 0:
        return "No data."

    unique_astronauts = Astronaut.objects.filter(mission_astronauts__spacecraft=spacecraft).distinct().count()

    return (f"The most used spacecraft is: {spacecraft.name}, manufactured by {spacecraft.manufacturer}, "
            f"used in {spacecraft.num_missions} missions, astronauts on missions: {unique_astronauts}.")


def decrease_spacecrafts_weight():
    spacecrafts = Spacecraft.objects.filter(
        mission__status='Planned',
        weight__gte=200.0
    ).distinct()

    num_of_spacecrafts_affected = spacecrafts.count()

    if num_of_spacecrafts_affected == 0:
        return "No changes in weight."

    with transaction.atomic():
        for spacecraft in spacecrafts:
            spacecraft.weight -= 200.0
            spacecraft.save()

    avg_weight = Spacecraft.objects.aggregate(avg_weight=Avg('weight'))['avg_weight']
    avg_weight = round(avg_weight, 1)

    return (f"The weight of {num_of_spacecrafts_affected} spacecrafts has been decreased. "
            f"The new average weight of all spacecrafts is {avg_weight}kg")



































