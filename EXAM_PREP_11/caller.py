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


def get_tournaments_by_surface_type(surface=None):
    if surface is None:
        return ''

    tournaments = ((Tournament.objects.filter(surface_type__icontains=surface)
                    .annotate(num_of_matches=Count('match')))
                   .order_by('-start_date'))

    tours = Tournament.objects.all()

    if not tournaments.exists() or not tours.exists():
        return ''

    result = []
    for t in tournaments:
        result.append(f"Tournament: {t.name}, start date: {t.start_date}, matches: {t.num_of_matches}")

    return '\n'.join(result)


def get_latest_match_info():
    matches = Match.objects.all().select_related('tournament').order_by('-date_played', '-id')
    match = matches.first()

    if not match:
        return ''

    players_in_match = []
    for p in match.players.all().order_by('full_name'):
        players_in_match.append(p.full_name)
    match_winner = match.winner

    result = (f"Latest match played on: {match.date_played}, "
              f"tournament: {match.tournament.name}, "
              f"score: {match.score}, "
              f"players: {players_in_match[0]} vs {players_in_match[1]}, "
              f"winner: {match_winner if match_winner else 'TBA'}, "
              f"summary: {match.summary}")

    return result


def get_matches_by_tournament(tournament_name=None):
    if tournament_name is None:
        return "No matches found."

    matches = (Match.objects.select_related('tournament')
               .filter(tournament__name__exact=tournament_name)).order_by('-date_played')

    if not matches.exists():
        return "No matches found."

    result = []
    for match in matches:
        result.append(f"Match played on: {match.date_played}, "
                      f"score: {match.score}, "
                      f"winner: {match.winner.full_name if match.winner else 'TBA'}")

    return '\n'.join(result)


