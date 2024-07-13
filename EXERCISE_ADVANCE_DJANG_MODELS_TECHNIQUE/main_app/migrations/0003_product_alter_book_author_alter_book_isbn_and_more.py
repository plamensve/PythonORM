# Generated by Django 5.0.4 on 2024-07-12 18:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_book_movie_music'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5, 'Author must be at least 5 characters long')]),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(6, 'ISBN must be at least 6 characters long')]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(8, 'Director must be at least 8 characters long')]),
        ),
        migrations.AlterField(
            model_name='music',
            name='artist',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(9, 'Artist must be at least 9 characters long')]),
        ),
        migrations.CreateModel(
            name='DiscountedProduct',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main_app.product',),
        ),
    ]