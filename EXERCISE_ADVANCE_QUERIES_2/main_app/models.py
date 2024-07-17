from datetime import datetime, timedelta

from django.db import models
from django.db.models import Q, F

from main_app.managers import RealEstateListingManager, VideoGameManager
from main_app.validators import rating_validator, release_year_validator


# Create your models here.


class RealEstateListing(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('House', 'House'),
        ('Flat', 'Flat'),
        ('Villa', 'Villa'),
        ('Cottage', 'Cottage'),
        ('Studio', 'Studio'),
    ]

    property_type = models.CharField(max_length=100, choices=PROPERTY_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    location = models.CharField(max_length=100)

    objects = RealEstateListingManager()


class VideoGame(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('RPG', 'RPG'),
        ('Adventure', 'Adventure'),
        ('Sports', 'Sports'),
        ('Strategy', 'Strategy'),
    ]

    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    release_year = models.PositiveIntegerField(validators=[release_year_validator])
    rating = models.DecimalField(max_digits=2, decimal_places=1, validators=[rating_validator])

    objects = VideoGameManager()

    def __str__(self):
        return self.title


class BillingInfo(models.Model):
    address = models.CharField(max_length=200)


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    billing_info = models.OneToOneField(BillingInfo, on_delete=models.CASCADE)

    @staticmethod
    def get_invoices_with_prefix(prefix: str):
        invoice_object = Invoice.objects.select_related('billing_info').filter(invoice_number__startswith=prefix)

        return invoice_object

    @staticmethod
    def get_invoices_sorted_by_number():
        invoice_object = Invoice.objects.all().select_related('billing_info').order_by('invoice_number')

        return invoice_object

    @staticmethod
    def get_invoice_with_billing_info(invoice_number: str):
        invoice_object = Invoice.objects.select_related('billing_info').get(invoice_number=invoice_number)

        return invoice_object


class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.ManyToManyField(Technology, related_name='projects')

    def get_programmers_with_technologies(self):
        return self.programmer.prefetch_related('projects__technologies_used')


class Programmer(models.Model):
    name = models.CharField(max_length=100)
    projects = models.ManyToManyField(Project, related_name='programmer')

    def get_projects_with_technologies(self):
        return self.projects.prefetch_related('technologies_used')


class Task(models.Model):
    PRIORITIES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITIES)
    is_completed = models.BooleanField(default=False)
    creation_date = models.DateField()
    completion_date = models.DateField()

    @staticmethod
    def ongoing_high_priority_tasks():
        task = Task.objects.filter(
            Q(priority='High') & Q(is_completed=False) & Q(completion_date__gt=F('creation_date')
        ))
        return task

    @classmethod
    def completed_mid_priority_tasks(cls):
        task = Task.objects.filter(
            Q(priority='Medium') & Q(is_completed=True)
        )
        return task

    @classmethod
    def search_tasks(cls, query: str):
        contain_the_query = Task.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return contain_the_query

    @classmethod
    def recent_completed_tasks(cls, days: int):
        tasks = Task.objects.filter(
            is_completed=True,
            completion_date__gte=F('creation_date') - timedelta(days=days)
        )
        return tasks

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    difficulty_level = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()

    @classmethod
    def get_long_and_hard_exercises(cls):
        ex = Exercise.objects.filter(duration_minutes__gt=30, difficulty_level__gte=10)
        return ex

    @classmethod
    def get_short_and_easy_exercises(cls):
        ex = Exercise.objects.filter(duration_minutes__lt=15, difficulty_level__lt=5)
        return ex

    @classmethod
    def get_exercises_within_duration(cls, min_duration: int, max_duration: int):
        ex = Exercise.objects.filter(duration_minutes__gte=min_duration, duration_minutes__lte=max_duration)
        return ex

    @classmethod
    def get_exercises_with_difficulty_and_repetitions(cls, min_difficulty: int, min_repetitions: int):
        ex = Exercise.objects.filter(difficulty_level__gte=min_difficulty, repetitions__gte=min_repetitions)
        return ex


























