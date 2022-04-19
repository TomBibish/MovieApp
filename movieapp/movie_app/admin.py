from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(MovieData)
# admin.site.register(MovieGenres)
# admin.site.register(Genre)
admin.site.register(Recommendations)
admin.site.register(PersonalWatchList)
