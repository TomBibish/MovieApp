
# the following 4 lines setup and initialize Django app with your default app settings
# after calling these lines you can actually access DB using Django Models
import csv
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movieapp.settings")
import django
django.setup()

from movie_app.models import *

with open('imdb_top_1000.csv', 'rt', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for row in reader:
            movie = MovieData(
                poster_link=row[0],
                title=row[1],
                released_year=row[2],
                duration_in_min=row[4],
                genre=row[5],
                imdb_rating=row[6],
                overview=row[7],
                director=row[9],
                star1=row[10],
                star2=row[11],
                star3=row[12],
                star4=row[13]
            )
            movie.save()


