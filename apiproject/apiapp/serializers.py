from rest_framework import serializers 
from apiapp.models import Movie 

class MovieSerializer(serializers.ModelSerializer): 
   
 
    class Meta:
        model = Movie
        fields = [
            'title',
            'imdb_score',
            'popularity',
            'movie_id',
            'genres',
            'director',
        ]
        ordering = ['id', '-imdb_score', 'title','-popularity', 'genres','director']