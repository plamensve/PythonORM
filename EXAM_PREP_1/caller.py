import os
import django
from django.db.models import Q, Count, Max, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Director, Actor


def get_directors(search_name=None, search_nationality=None):
    result = []
    if search_name and search_nationality:
        director = Director.objects.filter(
            Q(full_name__icontains=search_name) & Q(nationality__icontains=search_nationality)
        ).order_by('full_name')
        for d in director:
            result.append(f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}")
    elif search_name:
        director = Director.objects.filter(
            full_name__icontains=search_name).order_by('full_name')
        for d in director:
            result.append(f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}")
    elif search_nationality:
        director = Director.objects.filter(
            nationality__icontains=search_nationality).order_by('full_name')
        for d in director:
            result.append(f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}")
    else:
        pass

    if result:
        return '\n'.join(result)
    else:
        return ""


def get_top_director():
    max_movies = Director.objects.annotate(number_of_movies=Count('director_movies')
                                           ).aggregate(max_movies=Max('number_of_movies'))['max_movies']

    top_directors = Director.objects.annotate(number_of_movies=Count('director_movies')
                                              ).filter(number_of_movies=max_movies
                                                       ).order_by('full_name').first()

    if top_directors:
        return f"Top Director: {top_directors.full_name}, movies: {max_movies}."
    else:
        return ''


def get_top_actor():
    actor = Actor.objects.prefetch_related('starring_movies') \
        .annotate(
        num_of_movies=Count('starring_movies'),
        movies_avg_rating=Avg('starring_movies__rating')) \
        .order_by('-num_of_movies', 'full_name') \
        .first()

    if not actor or not actor.num_of_movies:
        return ""

    movies = ", ".join(movie.title for movie in actor.starring_movies.all() if movie)

    return f"Top Actor: {actor.full_name}, starring in movies: {movies}, " \
           f"movies average rating: {actor.movies_avg_rating:.1f}"

