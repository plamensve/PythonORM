import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import TennisPlayer
from django.db.models import Q, Count


def get_tennis_players(search_name=None, search_country=None):
    global query

    if search_name is None and search_country is None:
        return ''

    if search_name and search_country:
        query = Q(full_name__icontains=search_name) & Q(country__icontains=search_country)

    elif search_name and search_country is None:
        query = Q(full_name__icontains=search_name)

    elif search_name is None and search_country:
        query = Q(country__icontains=search_country)

    players = TennisPlayer.objects.filter(query).order_by('ranking')

    if not players.exists():
        return ''

    result = []
    for p in players:
        result.append(f"Tennis Player: {p.full_name}, country: {p.country}, ranking: {p.ranking}")

    return '\n'.join(result)


def get_top_tennis_player():
    player = TennisPlayer.objects.get_tennis_players_by_wins_count().first()

    if not player:
        return ''

    return f"Top Tennis Player: {player.full_name} with {player.number_of_wins} wins."


def get_tennis_player_by_matches_count():
    player = ((TennisPlayer.objects.annotate(matches_count=Count('match_players'))
               .order_by('-matches_count', 'ranking'))
              .first())

    if not player or not player.matches_count:
        return ''

    return f"Tennis Player: {player.full_name} with {player.matches_count} matches played."


print(get_tennis_player_by_matches_count())
