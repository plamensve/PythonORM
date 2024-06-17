# Generated by Django 5.0.6 on 2024-06-17 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('employees_count', models.PositiveIntegerField(default=1, verbose_name='Employees Count')),
                ('location', models.CharField(blank=True, choices=[('Sofia', 'Sofia'), ('Plovdiv', 'Plovdiv'), ('Burgas', 'Burgas'), ('Varna', 'Varna')], max_length=20)),
                ('last_edited_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email_address', models.EmailField(max_length=254)),
                ('photo', models.URLField()),
                ('birth_date', models.DateField()),
                ('works_full_time', models.BooleanField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('budget', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('duration_in_days', models.PositiveIntegerField(blank=True, verbose_name='Duration in Days')),
                ('estimated_hours', models.FloatField(blank=True, default=0.0, verbose_name='Estimated Hours')),
                ('start_date', models.DateField(blank=True, default=datetime.date(2024, 6, 17), verbose_name='Start Date')),
                ('created_on', models.DateField(editable=False, verbose_name=datetime.date(2024, 6, 17))),
                ('last_edited_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
