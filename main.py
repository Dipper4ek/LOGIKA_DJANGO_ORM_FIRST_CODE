import django_setup

from games.models import Genre, Game

# Створення жанрів
action = Genre.objects.create(name="Action")
rpg = Genre.objects.create(name="RPG")

# Створення гри
game1 = Game.objects.create(title="The Witcher 3", release_year=2015, rating=9.8)
game1.genres.add(action, rpg)

game2 = Game.objects.create(title="Cyberpunk 2077", release_year=2020, rating=7.5)
game2.genres.add(action, rpg)
