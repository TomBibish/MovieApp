from django import forms
from django.forms import Select, Textarea, TextInput, DateInput, HiddenInput, CheckboxInput
from .models import *


class MyDateWidget(DateInput):
    input_type = 'date'


class Recommenderform(forms.ModelForm):
    movie = forms.ModelChoiceField(queryset=MovieData.objects.all(),
                                   widget=HiddenInput(attrs={'class': 'form-control'}))
    recommender = forms.ModelChoiceField(queryset=User.objects.all(),
                                         widget=HiddenInput(attrs={'class': 'form-control'}))
    recommend_to = forms.ModelChoiceField(queryset=User.objects.all(),
                                          widget=Select(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    date_recommended = forms.DateField(widget=MyDateWidget())
    is_watched_by_receiver = forms.BooleanField(widget=HiddenInput(attrs={'class': 'form-control'}))
    date_watched_by_receiver = forms.DateField(widget=HiddenInput(attrs={'class': 'form-control'}))
    receiver_rating = forms.CharField(widget=HiddenInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(Recommenderform, self).__init__(*args, **kwargs)
        self.fields['is_watched_by_receiver'].required = False
        self.fields['date_watched_by_receiver'].required = False
        self.fields['receiver_rating'].required = False

    class Meta:
        model = Recommendations
        fields = ['movie', 'recommender', 'recommend_to', 'message',
                  'date_recommended', 'is_watched_by_receiver', 'date_watched_by_receiver', 'receiver_rating']


class RespondForm(forms.ModelForm):
    movie = forms.ModelChoiceField(queryset=MovieData.objects.all(),
                                   widget=HiddenInput(attrs={'class': 'form-control'}))
    recommender = forms.ModelChoiceField(queryset=User.objects.all(),
                                         widget=HiddenInput(attrs={'class': 'form-control'}))
    recommend_to = forms.ModelChoiceField(queryset=User.objects.all(),
                                          widget=HiddenInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=HiddenInput(attrs={'class': 'form-control'}))
    date_recommended = forms.DateField(widget=HiddenInput())
    is_watched_by_receiver = forms.BooleanField(widget=CheckboxInput())
    date_watched_by_receiver = forms.DateField(widget=MyDateWidget())
    receiver_rating = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Recommendations
        fields = ['movie', 'recommender', 'recommend_to', 'message',
                  'date_recommended', 'is_watched_by_receiver', 'date_watched_by_receiver', 'receiver_rating']


class WatchListForm(forms.ModelForm):
    movie = forms.ModelChoiceField(queryset=MovieData.objects.all(),
                                   widget=HiddenInput(attrs={'class': 'form-control'}))
    user = forms.ModelChoiceField(queryset=User.objects.all(),
                                  widget=HiddenInput(attrs={'class': 'form-control'}))
    date_watch = forms.DateField(widget=MyDateWidget())
    liked = forms.BooleanField(widget=CheckboxInput())

    class Meta:
        model = PersonalWatchList
        fields = ['movie', 'user', 'date_watch', 'liked']
