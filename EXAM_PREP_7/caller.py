import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import TennisPlayer, Tournament, Match
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


def get_tournaments_by_surface_type(surface=None):
    if surface is None:
        return ''

    tournament = Tournament.objects.filter(surface_type__icontains=surface).order_by('-start_date')
    if not tournament:
        return ''

    result = []
    for t in tournament:
        result.append(f"Tournament: {t.name}, start date: {t.start_date}, matches: {t.matches.count()}")

    return '\n'.join(result)


def get_latest_match_info():
    match = (Match.objects.all()
             .order_by('-date_played', 'id')
             .select_related('tournament')
             .prefetch_related('players')
             .first())

    if not match:
        return ''

    players = match.players.all().order_by('full_name')
    players_list = ' vs '.join(player.full_name for player in players)
    winner_name = match.winner.full_name if match.winner else 'TBA'

    result = (f"Latest match played on: {match.date_played}, "
              f"tournament: {match.tournament.name}, "
              f"score: {match.score}, "
              f"players: {players_list}, "
              f"winner: {winner_name}, "
              f"summary: {match.summary}")

    return result


def get_matches_by_tournament(tournament_name=None):
    if tournament_name is None:
        return "No matches found."

    matches = (Match.objects.filter(tournament__name__exact=tournament_name)
               .annotate(matches_count=Count('winner'))).order_by('-date_played')

    tournament = Tournament.objects.filter(name__exact=tournament_name)
    tournaments = Tournament.objects.all()
    if not matches or not tournament or not tournaments:
        return "No matches found."

    result = []
    for match in matches:
        result.append(f"Match played on: {match.date_played}, "
                      f"score: {match.score}, "
                      f"winner: {match.winner.full_name if match.winner else 'TBA'}")

    return '\n'.join(result)



