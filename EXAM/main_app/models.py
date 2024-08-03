from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator, MaxLengthValidator
from django.db import models

from main_app.manager import AstronautManager


def validate_only_digits(value):
    if not value.isdigit():
        raise ValidationError('This field must contain only digits.')


class Astronaut(models.Model):
    name = models.CharField(
        max_length=120,
        validators=[
            MinLengthValidator(2)
        ]
    )

    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[validate_only_digits],
    )

    is_active = models.BooleanField(
        default=True
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    spacewalks = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    objects = AstronautManager()

class Spacecraft(models.Model):
    name = models.CharField(
        max_length=120,
        validators=[
            MinLengthValidator(2)
        ]
    )

    manufacturer = models.CharField(
        max_length=100
    )

    capacity = models.SmallIntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )

    weight = models.FloatField(
        validators=[
            MinValueValidator(0.0)
        ]
    )

    launch_date = models.DateField()

    updated_at = models.DateTimeField(
        auto_now=True
    )


class Mission(models.Model):
    class StatusChoices(models.TextChoices):
        PLANNED = 'Planned', 'Planned'
        ONGOING = 'Ongoing', 'Ongoing'
        COMPLETED = 'Completed', 'Completed'

    name = models.CharField(
        max_length=120,
        validators=[
            MinLengthValidator(2)
        ]
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    status = models.CharField(
        default='Planned',
        max_length=9,
        validators=[
            MaxLengthValidator(9)
        ],
        choices=StatusChoices.choices
    )

    launch_date = models.DateField()

    updated_at = models.DateTimeField(
        auto_now=True
    )

    spacecraft = models.ForeignKey(
        Spacecraft,
        on_delete=models.CASCADE
    )

    astronauts = models.ManyToManyField(
        Astronaut,
        related_name='mission_astronauts'
    )

    commander = models.ForeignKey(
        Astronaut,
        null=True,
        on_delete=models.SET_NULL,
        related_name='mission_commander'
    )
