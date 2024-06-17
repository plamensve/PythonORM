# Generated by Django 5.0.6 on 2024-06-17 19:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_department_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='budget',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='duration_in_days',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Duration in Days'),
        ),
        migrations.AlterField(
            model_name='project',
            name='estimated_hours',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='Estimated Hours'),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.date(2024, 6, 17), null=True, verbose_name='Start Date'),
        ),
    ]
