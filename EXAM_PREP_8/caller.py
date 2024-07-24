import os
import django
from django.db.models import Q, Count, Max

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Director, Actor, Movie
from django.db.models import Q, F


def get_directors(search_name=None, search_nationality=None):
    global query

    if search_name is None and search_nationality is None:
        return ''

    if search_name and search_nationality:
        query = Q(full_name__icontains=search_name) & Q(nationality__icontains=search_nationality)
    elif search_name:
        query = Q(full_name__icontains=search_name)
    elif search_nationality:
        query = Q(nationality__icontains=search_nationality)

    directors = Director.objects.filter(query)
    if not directors:
        return ''

    result = []
    for d in directors.order_by('full_name'):
        result.append(f"Director: {d.full_name}, "
                      f"nationality: {d.nationality}, "
                      f"experience: {d.years_of_experience}")

    return '\n'.join(result)


def get_top_director():
    director = Director.objects.get_directors_by_movies_count().first()

    if not director:
        return ''

    return f"Top Director: {director.full_name}, movies: {director.number_of_movies}."


from django.db.models import Count, Avg


def get_top_actor():
    actor = (Actor.objects.annotate(number_of_movies=Count('movie__starring_actor'))
             .order_by('-number_of_movies', 'full_name')
             .first())

    if not actor or actor.number_of_movies == 0:
        return ''

    movies = actor.movie_set.all()
    if not movies.exists():
        return ''

    cumulative_rating = sum(m.rating for m in movies)
    avg_rating = cumulative_rating / len(movies)
    movies_titles = [m.title for m in movies]

    result = (f"Top Actor: {actor.full_name}, "
              f"starring in movies: {', '.join(movies_titles)}, "
              f"movies average rating: {avg_rating:.1f}")

    return result


def get_actors_by_movies_count():
    actors = (Actor.objects.annotate(number_of_movies=Count('actors'))
              .order_by('-number_of_movies', 'full_name'))[:3]

    if not actors:
        return ''

    result = []
    for actor in actors:
        if not actor.actors.all():
            return ''

        result.append(f"{actor.full_name}, participated in {len(actor.actors.all())} movies")
    return '\n'.join(result)


def get_top_rated_awarded_movie():
    movie = ((Movie.objects.filter(is_awarded=True)
              .annotate(max_rating=Max('rating'))
              .order_by('-max_rating', 'title'))
             .first())

    if not movie:
        return ''

    result = (f"Top rated awarded movie: {movie.title}, "
              f"rating: {'N/A' if not movie.max_rating else movie.max_rating:.1f}. "
              f"Starring actor: {'N/A' if not movie.starring_actor else movie.starring_actor.full_name}. "
              f"Cast: {', '.join([a.full_name for a in Actor.objects.filter(actors__title=movie.title)])}.")

    return result


def increase_rating():
    movies = Movie.objects.filter(is_classic=True, rating__lt=10.0).update(rating=F('rating') + 0.1)
    if movies == 0:
        return "No ratings increased."

    return f"Rating increased for {movies} movies."







































