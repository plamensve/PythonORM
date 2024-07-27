import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import TennisPlayer, Tournament, Match
from django.db.models import Q, Count


def get_tennis_players(search_name=None, search_country=None):
    global players

    if search_name is None and search_country is None:
        return ''

    if search_name and search_country:
        players = TennisPlayer.objects.filter(full_name__icontains=search_name, country__icontains=search_country)

    elif search_name:
        players = TennisPlayer.objects.filter(full_name__icontains=search_name)

    elif search_country:
        players = TennisPlayer.objects.filter(country__icontains=search_country)

    players = players.order_by('ranking')

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
    player = (TennisPlayer.objects.annotate(num_of_matches=Count('TennisPlayers'))
              .order_by('-num_of_matches', 'ranking')
              .first())

    if not player or player.num_of_matches == 0:
        return ''

    return f"Tennis Player: {player.full_name} with {player.num_of_matches} matches played."


print(get_tennis_player_by_matches_count())
