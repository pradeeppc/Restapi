from django.shortcuts import render 
from rest_framework import status 
from apiapp.models import Movie 
from apiapp.serializers import MovieSerializer
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from django.http import Http404,JsonResponse,HttpResponse
 
@api_view(['GET', 'POST']) 
def movie_list(request): 
    if request.method == 'GET': 
        movies = Movie.objects.all() 
        movies_serializer = MovieSerializer(movies, many=True) 
        return Response(movies_serializer.data) 
 
    elif request.method == 'POST': 
        movie_serializer = MovieSerializer(data=request.data) 
        if movie_serializer.is_valid(): 
            movie_serializer.save() 
            return Response(movie_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
 
@api_view(['GET', 'PUT', 'DELETE']) 
def movie_detail(request): 
    try: 
        movie = Movie.objects.get(pk=pk) 
    except Movie.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        movie_serializer = MovieSerializer(movie) 
        return Response(movie_serializer.data) 
 
    elif request.method == 'PUT': 
        movie_serializer = MovieSerializer(movie, data=request.data) 
        if movie_serializer.is_valid(): 
            movie_serializer.save() 
            return Response(movie_serializer.data) 
        return Response(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        movie.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(["GET"])
def movie_detail(title_data):   #search movie by title
    title = (title_data.body).decode('UTF-8')
    try:
        title_data = movie_detail.objects.filter(title__icontains=title)
        if title_data.values()[0] is not None:
            return JsonResponse(title_data.values()[0], safe=False)
    except Exception as yt:
        print('not found in local db',yt)
       
    