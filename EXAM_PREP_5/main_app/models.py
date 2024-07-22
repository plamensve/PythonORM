from datetime import timedelta

from django.db import models
from django.db.models import Q, F

from main_app.custom_manager import RealEstateListingManager, VideoGameManager
from main_app.validators import rating_validator, year_validator


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

    title = models.CharField(
        max_length=100
    )

    genre = models.CharField(
        max_length=100,
        choices=GENRE_CHOICES
    )

    release_year = models.PositiveIntegerField(
        validators=[year_validator]
    )

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[rating_validator]
    )

    def __str__(self):
        return self.title

    objects = VideoGameManager()


class BillingInfo(models.Model):
    address = models.CharField(max_length=200)


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    billing_info = models.OneToOneField(BillingInfo, on_delete=models.CASCADE)

    @classmethod
    def get_invoices_with_prefix(cls, prefix: str):
        return Invoice.objects.filter(invoice_number__startswith=prefix)

    @classmethod
    def get_invoices_sorted_by_number(cls):
        return Invoice.objects.all().order_by('invoice_number')

    @classmethod
    def get_invoice_with_billing_info(cls, invoice_number: str):
        return Invoice.objects.get(invoice_number=invoice_number)


class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.ManyToManyField(Technology, related_name='projects')

    def get_programmers_with_technologies(self):
        return self.programmers.prefetch_related('projects__technologies_used').all()


class Programmer(models.Model):
    name = models.CharField(max_length=100)
    projects = models.ManyToManyField(Project, related_name='programmers')

    def get_projects_with_technologies(self):
        return self.projects.prefetch_related('technologies_used').all()


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

    @classmethod
    def ongoing_high_priority_tasks(cls):
        query = Q(priority='High') & Q(is_completed=False) & Q(completion_date__gt=F('creation_date'))
        tasks = cls.objects.filter(query)
        return tasks

    @classmethod
    def completed_mid_priority_tasks(cls):
        query = Q(priority='Medium') & Q(is_completed=True)
        tasks = cls.objects.filter(query)
        return tasks

    @classmethod
    def search_tasks(cls, query: str):
        filter_query = Q(title__icontains=query) | Q(description__icontains=query)
        tasks = cls.objects.filter(filter_query)

        return tasks

    @classmethod
    def recent_completed_tasks(cls, days: int):
        query = Q(is_completed=True) & Q(completion_date__gte=F('creation_date') - timedelta(days=days))
        tasks = cls.objects.filter(query)
        return tasks


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    difficulty_level = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()
