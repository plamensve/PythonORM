# Generated by Django 5.0.4 on 2024-07-03 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_studentenrollment_enrollment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentenrollment',
            name='enrollment_date',
            field=models.DateField(default=datetime.datetime(2024, 7, 3, 9, 52, 17, 444866, tzinfo=datetime.timezone.utc)),
        ),
    ]
