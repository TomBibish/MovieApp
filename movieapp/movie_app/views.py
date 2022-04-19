from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.template import RequestContext
from .forms import Recommenderform, RespondForm, WatchListForm
from .models import *
# Create your views here.


def index(request):
    movie_query_set = MovieData.objects.all()
    if 'filter_movie' in request.GET and request.GET['filter_movie']:
        movie_query_set = movie_query_set.filter(Q(title__icontains=request.GET['filter_movie']) |
                                                 Q(genre__icontains=request.GET['filter_movie']) |
                                                 Q(director__icontains=request.GET['filter_movie']) |
                                                 Q(star1__icontains=request.GET['filter_movie']) |
                                                 Q(star2__icontains=request.GET['filter_movie']) |
                                                 Q(star3__icontains=request.GET['filter_movie']) |
                                                 Q(star4__icontains=request.GET['filter_movie'])
                                                 )
    if 'sort_by_year' in request.GET:
        if request.GET['sort_by_year'] == "desc":
            movie_query_set = movie_query_set.order_by('released_year')
        else:
            movie_query_set = movie_query_set.order_by('-released_year')
    if 'sort_by_rating' in request.GET:
        if request.GET['sort_by_rating'] == "desc":
            movie_query_set = movie_query_set.order_by('imdb_rating')
        else:
            movie_query_set = movie_query_set.order_by('-imdb_rating')
    movie_paginator = Paginator(movie_query_set, 50)
    page_number = request.GET.get('page')
    page = movie_paginator.get_page(page_number)
    return render(request=request,
                  template_name='movie_app/index.html',
                  context={'page': page})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'movie_app/signup.html', {'form': form})


@login_required
def movie_details(request, movie_id):
    movie = MovieData.objects.get(pk=movie_id)
    return render(request=request,
                  template_name='movie_app/movie_details.html',
                  context={'movie': movie})


@login_required
def recommend_to_me(request, user_id):
    recommend = Recommendations.objects.all()
    recommend = recommend.filter(recommend_to=user_id)
    return render(request=request,
                  template_name="movie_app/my_recommends.html",
                  context={'recommends': recommend})


@login_required
def recommend_by_me(request, user_id):
    recommend = Recommendations.objects.all()
    recommend = recommend.filter(recommender=user_id)
    return render(request=request,
                  template_name="movie_app/recommends_by_me.html",
                  context={'recommends': recommend})


@login_required
def recommend_to_movie(request, movie_id):
    movie = MovieData.objects.get(pk=movie_id)
    if request.method == 'GET':
        form = Recommenderform(initial={'recommender': request.user,
                                        'movie': movie})
        return render(request, template_name='movie_app/recommend_to_movie.html', context={'form': form})
    elif request.method == 'POST':
        form = Recommenderform(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, template_name='movie_app/recommend_to_movie.html', context={'form': form})


@login_required
def respond_to_recommend(request, recommend_id):
    recommend = Recommendations.objects.get(pk=recommend_id)
    if request.method == 'GET':
        form = RespondForm(instance=recommend)
        return render(request, template_name='movie_app/add_to_watch_list.html', context={'form': form})
    elif request.method == 'POST':
        form = RespondForm(data=request.POST, instance=recommend)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, template_name='movie_app/add_to_watch_list.html', context={'form': form})


@login_required
def add_to_watch_list(request, movie_id):
    movie = MovieData.objects.get(pk=movie_id)
    if request.method == 'GET':
        form = WatchListForm(initial={'user': request.user,
                                      'movie': movie})
        return render(request, template_name='movie_app/add_to_watch_list.html', context={'form': form})
    elif request.method == 'POST':
        form = WatchListForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, template_name='movie_app/add_to_watch_list.html', context={'form': form})


@login_required
def watch_list(request, user_id):
    my_watch_list = PersonalWatchList.objects.all()
    my_watch_list = my_watch_list.filter(user=user_id)
    return render(request=request,
                  template_name="movie_app/watch_list.html",
                  context={'my_watch_list': my_watch_list})