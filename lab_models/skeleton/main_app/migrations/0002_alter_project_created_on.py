# Generated by Django 5.0.6 on 2024-06-17 19:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created_on',
            field=models.DateTimeField(editable=False, verbose_name=datetime.date(2024, 6, 17)),
        ),
    ]
