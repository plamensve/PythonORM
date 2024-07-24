from django.core.validators import MinValueValidator, MinLengthValidator, MaxValueValidator
from django.db import models

from main_app.manager import DirectorManager
from main_app.mixins import BaseInfoMixin, AwardedUpdatedMixin


class Director(BaseInfoMixin):
    years_of_experience = models.SmallIntegerField(
        validators=[MinValueValidator(0)],
    default=0)

    objects = DirectorManager()

class Actor(BaseInfoMixin, AwardedUpdatedMixin):
    pass


class Movie(AwardedUpdatedMixin):
    class GenreChoices(models.TextChoices):
        ACTION = 'Action', 'Action'
        COMEDY = 'Comedy', 'Comedy'
        DRAMA = 'Drama', 'Drama'
        OTHER = 'Other', 'Other'

    title = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(5)])

    release_date = models.DateField()

    storyline = models.TextField(
        null=True,
        blank=True
    )

    genre = models.CharField(
        max_length=6,
        default='Other',
        choices=GenreChoices.choices)

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0)
        ],
        default=0.0
    )

    is_classic = models.BooleanField(
        default=False
    )

    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE
    )

    starring_actor = models.ForeignKey(
        Actor,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    actors = models.ManyToManyField(
        Actor,
        related_name='actors'
    )






















