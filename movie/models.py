from django.db import models


class Genre_model(models.Model):
    genre_name=models.CharField(max_length=100)
    genre_description=models.TextField(null=True)

    def __str__(self):
        return self.genre_name



class Movie_model(models.Model):
    movie_name=models.CharField(max_length=100)
    movie_language=models.CharField(max_length=100)
    movie_description=models.TextField(null=True)
    movie_duration=models.CharField(max_length=100)
    movie_genre=models.ForeignKey(Genre_model,on_delete=models.CASCADE)


    

