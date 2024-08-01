import os
from datetime import date

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Director, Actor, Movie
from django.db.models import Q, Count, Sum


def get_directors(search_name=None, search_nationality=None):
    global query

    if not search_name and not search_nationality:
        return ''

    if search_name and not search_nationality:
        query = Q(full_name__icontains=search_name)

    elif not search_name and search_nationality:
        query = Q(nationality__icontains=search_nationality)

    elif search_name and search_nationality:
        query = Q(full_name__icontains=search_name) & Q(nationality__icontains=search_nationality)

    directors = Director.objects.filter(query)

    if not directors.exists():
        return ''

    result = []
    for director in directors.order_by('full_name'):
        result.append(f"Director: {director.full_name}, "
                      f"nationality: {director.nationality}, "
                      f"experience: {director.years_of_experience}")

    return '\n'.join(result)


def get_top_director():
    director = Director.objects.get_directors_by_movies_count().first()

    if not director:
        return ''

    return f"Top Director: {director.full_name}, movies: {director.number_of_movies}."


def get_top_actor():
    actor_with_most_movies = (Movie.objects.all().select_related('starring_actor')
                              .annotate(movies_count=Count('starring_actor'))
                              .order_by('-movies_count')).first()

    if not actor_with_most_movies or actor_with_most_movies.movies_count == 0:
        return ''

    actor = actor_with_most_movies.starring_actor
    all_movies = actor.movie_set.all()
    if not all_movies.exists():
        return ''

    avg_rating_cumulative = 0

    for m in all_movies:
        avg_rating_cumulative += m.rating
    avg_rating = avg_rating_cumulative / len(all_movies)

    return (f"Top Actor: {actor.full_name}, "
            f"starring in movies: {', '.join([m.title for m in all_movies])}, "
            f"movies average rating: {avg_rating:.1f}")


def get_actors_by_movies_count():
    top_actors = (Actor.objects.filter(actors_movie__gt=0)
                  .prefetch_related('actors_movie')
                  .annotate(count_of_movies=Count('actors_movie'))
                  .order_by('-count_of_movies', 'full_name'))[:3]

    if not top_actors:
        return ''

    result = []
    for a in top_actors:
        result.append(f"{a.full_name}, participated in {a.count_of_movies} movies")

    return '\n'.join(result)


def get_top_rated_awarded_movie():
    movie = (Movie.objects.filter(is_awarded=True)
             .select_related('starring_actor')
             .prefetch_related('actors')
             .order_by('-rating', 'title')
             .first())

    if not movie:
        return ''

    starring_actor = movie.starring_actor.full_name if movie.starring_actor else 'N/A'
    all_actors = movie.actors.all().order_by('full_name')
    cast = ', '.join(actor.full_name for actor in all_actors)

    result = (f"Top rated awarded movie: {movie.title}, "
              f"rating: {movie.rating:.1f}. "
              f"Starring actor: {starring_actor}. "
              f"Cast: {cast}")

    return result

print(get_top_rated_awarded_movie())






























