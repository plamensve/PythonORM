from django.db import models
from django.db.models import Count


class TennisPlayerManager(models.Manager):
    def get_tennis_players_by_wins_count(self):
        player = (self.annotate(number_of_wins=Count('match__winner'))
                  .order_by('-number_of_wins', 'full_name'))

        return player

