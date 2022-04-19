from django.urls import path
from . import views
from django.contrib.auth import  views as auth_views
urlpatterns = [
    path("", views.index),
    path('signup', views.signup, name='signup'),
    path('logout', auth_views.LogoutView.as_view()),
    path('login', auth_views.LoginView.as_view()),
    path('movie/<int:movie_id>', views.movie_details, name='movie_details'),
    path('my_recommends/<int:user_id>', views.recommend_to_me, name='recommend_to_me'),
    path('recommends_by_me/<int:user_id>', views.recommend_by_me, name='recommend_by_me'),
    path('recommend_to_movie/<int:movie_id>', views.recommend_to_movie, name='recommend_to_movie'),
    path('respond_to_recommend/<int:recommend_id>', views.respond_to_recommend, name='respond_to_recommend'),
    path('add_to_watch_list/<int:movie_id>', views.add_to_watch_list, name='add_to_watch_list'),
    path('watch_list/<int:user_id>', views.watch_list, name="watch_list")
]