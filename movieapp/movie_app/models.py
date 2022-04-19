from django.contrib.auth.models import User
from django.db import models

# Create your models here.
RATING_CHOICES = (
    ('1', '1 STARS'),
    ('2', '2 STARS'),
    ('3', '3 STARS'),
    ('4', '4 STARS'),
    ('5', '5 STARS')
)


# class Genre(models.Model):
#     name = models.CharField(max_length=56, null=False, blank=False)
#
#     def __str__(self):
#         return f"{self.name}"


# class Director(models.Model):
#     name = models.CharField(max_length=128, null=False, blank=False)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class Actor(models.Model):
#     name = models.CharField(max_length=128, null=False, blank=False)
#
#     def __str__(self):
#         return f"{self.name}"


class MovieData(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    poster_link = models.URLField()
    released_year = models.CharField(max_length=5, null=False, blank=False)
    duration_in_min = models.CharField(max_length=10, null=False, blank=False)
    genre = models.CharField(max_length=128, null=False, blank=False)
    imdb_rating = models.CharField(max_length=4, null=False, blank=False)
    overview = models.CharField(max_length=1280, null=False, blank=False)
    director = models.CharField(max_length=128, null=False, blank=False)
    star1 = models.CharField(max_length=128, null=False, blank=False)
    star2 = models.CharField(max_length=128, null=True, blank=True)
    star3 = models.CharField(max_length=128, null=True, blank=True)
    star4 = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return f'"{self.title}" by {self.director}'


# class MovieGenres(models.Model):
#     genre = models.ForeignKey(Genre, on_delete=models.RESTRICT)
#     movie = models.ForeignKey(MovieData, on_delete=models.RESTRICT)
#
#     def __str__(self):
#         return f"{self.movie} has genre: {self.genre}"


class PersonalWatchList(models.Model):
    movie = models.ForeignKey(MovieData, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    date_watch = models.DateField()
    liked = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f"Review of {self.movie} from {self.user}"


class Recommendations(models.Model):
    movie = models.ForeignKey(MovieData, on_delete=models.RESTRICT)
    recommender = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='recommender')
    recommend_to = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='recommend_to')
    message = models.CharField(max_length=526, blank=True, null=True)
    date_recommended = models.DateField()
    is_watched_by_receiver = models.BooleanField(null=True, blank=True)
    date_watched_by_receiver = models.DateField(null=True, blank=True)
    receiver_rating = models.CharField(max_length=1, choices=RATING_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"{self.movie} recommended by {self.recommender} to {self.recommend_to}"
