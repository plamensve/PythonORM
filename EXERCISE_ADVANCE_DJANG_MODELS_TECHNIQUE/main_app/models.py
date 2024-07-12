from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator, EmailValidator, RegexValidator, MinLengthValidator

from main_app.validators import check_name


class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[check_name])

    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(
                18, message="Age must be greater than or equal to 18")])

    email = models.EmailField(error_messages={'invalid': "Enter a valid email address"})

    phone_number = models.CharField(
        max_length=13,
        validators=[
            RegexValidator(regex=r'^\+359\d{9}$',
                           message="Phone number must start with '+359' followed by 9 digits")])  # Премахнете запетаята

    website_url = models.URLField(
        error_messages={'invalid': "Enter a valid URL"})


class BaseMedia(models.Model):
    class Meta:
        abstract = True
        ordering = ['-created_at', 'title']

    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Book(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = "Model Book"
        verbose_name_plural = "Models of type - Book"

    author = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(5, "Author must be at least 5 characters long")])

    isbn = models.CharField(
        max_length=20,
        unique=True,
        validators=[MinLengthValidator(6, "ISBN must be at least 6 characters long")])


class Movie(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = "Model Movie"
        verbose_name_plural = "Models of type - Movie"

    director = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(8, "Director must be at least 8 characters long")])


class Music(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = "Model Music"
        verbose_name_plural = "Models of type - Music"

    artist = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(9, "Artist must be at least 9 characters long")])
