import os
import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import RealEstateListing, VideoGame

# Run the custom manager methods
action_games = VideoGame.objects.games_by_genre('Action')
recent_games = VideoGame.objects.recently_released_games(2019)
average_rating = VideoGame.objects.average_rating()
highest_rated = VideoGame.objects.highest_rated_game()
lowest_rated = VideoGame.objects.lowest_rated_game()

# Print the results
print(action_games)
print(recent_games)
print(average_rating)
print(highest_rated)
print(lowest_rated)

