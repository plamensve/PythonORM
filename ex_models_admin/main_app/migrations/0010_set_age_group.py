# Generated by Django 5.0.4 on 2024-06-24 18:44

from django.db import migrations


def set_age_group(apps, schema_editor):
    person = apps.get_model('main_app', 'Person')

    people = person.objects.all()

    for p in people:
        if p.age <= 12:
            p.age_group = 'Child'
        elif 13 <= p.age <= 17:
            p.age_group = 'Teen'
        else:
            p.age_group = 'Adult'

        # person.save()
    person.objects.bulk_update(people, ['age_group'])


def reverse_set_age_group(apps, schema_editor):
    person = apps.get_model('main_app', 'Person')

    for person in person.objects.all():
        person.age_group = person._meta.get_field('age_group').default
        person.save()


class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0009_person'),
    ]

    operations = [
        migrations.RunPython(set_age_group, reverse_set_age_group)
    ]
