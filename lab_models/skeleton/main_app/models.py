import datetime

from django.db import models


class Employee(models.Model):
    name = models.CharField(
        max_length=30
    )
    email_address = models.EmailField()
    photo = models.URLField()
    birth_date = models.DateField()
    works_full_time = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)


class Department(models.Model):
    CITY_CHOICES = [
        ('Sofia', 'Sofia'),
        ('Plovdiv', 'Plovdiv'),
        ('Burgas', 'Burgas'),
        ('Varna', 'Varna')
    ]

    code = models.CharField(
        max_length=4,
        primary_key=True,
        unique=True
    )
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    employees_count = models.PositiveIntegerField(
        default=1,
        verbose_name='Employees Count',
    )
    location = models.CharField(
        max_length=20,
        blank=True,
        choices=CITY_CHOICES
    )
    last_edited_on = models.DateTimeField(
        auto_now=True,
        editable=False
    )


class Project(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    duration_in_days = models.PositiveIntegerField(
        verbose_name='Duration in Days',
        null=True,
        blank=True
    )

    estimated_hours = models.FloatField(
        blank=True,
        verbose_name='Estimated Hours',
        null=True
    )

    start_date = models.DateField(
        verbose_name='Start Date',
        blank=True,
        default=datetime.date.today(),
        null=True
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    last_edited_on = models.DateTimeField(
        auto_now=True,
        editable=False
    )
