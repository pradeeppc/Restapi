from django.db import models

class Movie(models.Model):
    
    title = models.CharField(max_length=150)
    imdb_score = models.FloatField(default=0.0)
    popularity = models.FloatField(null=True, blank=True)
    movie_id = models.CharField(max_length=30)
    genres = models.CharField(max_length=120)
    director = models.CharField(max_length=100)
    

    def __str__(self):
        return self.title