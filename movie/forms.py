from django import forms
from movie.models import Genre_model,Movie_model

class Genre_form(forms.ModelForm):
    class Meta:
        model=Genre_model
        fields="__all__"
        widgets={
            'genre_name':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter New Genre"}),
            'genre_description':forms.Textarea(attrs={"class":"form-control","placeholder":"Enter About Genre"}),

            
            }


class Movie_form(forms.ModelForm):
    class Meta:
        model=Movie_model
        fields="__all__"
        widgets={
            'movie_name':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Movie Name"}),
            'movie_language':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Movie Language"}),
            'movie_description':forms.Textarea(attrs={"class":"form-control","placeholder":"Enter About Movie"}),
            'movie_duration':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Movie Duration"}),
            
            }

    
