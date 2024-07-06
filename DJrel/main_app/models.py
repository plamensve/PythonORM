from datetime import timedelta

from django.db import models


class Author(models.Model):
    name = models.CharField(
        max_length=40
    )


class Book(models.Model):
    title = models.CharField(
        max_length=40,
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
    )