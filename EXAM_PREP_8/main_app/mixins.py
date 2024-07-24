from django.core.validators import MinLengthValidator
from django.db import models


class BaseInfoMixin(models.Model):
    class Meta:
        abstract = True

    full_name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)])

    birth_date = models.DateField(
        default='1900-01-01')

    nationality = models.CharField(max_length=50, default='Unknown')


class AwardedUpdatedMixin(models.Model):
    class Meta:
        abstract = True

    is_awarded = models.BooleanField(
        default=False)

    last_updated = models.DateTimeField(
        auto_now=True)