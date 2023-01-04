from rest_framework.response import Response
from rest_framework.decorators import api_view
from django import setup

import movie_app.serializers
from movie_app.models import Movie, Director, Review
from movie_app.serializers import MovieSerializer, DirectorSerializer, ReviewSerializer
from rest_framework.status import HTTP_200_OK


@api_view(['GET'])
def movies_show_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def movie_detail_view(request, **a):
    if request.method == 'GET':
        movie = Movie.objects.get(id=a['id'])

        data = movie_app.serializers.MovieSerializer(movie).data
        return Response(data=data, status=HTTP_200_OK)




@api_view(['GET'])
def directors_views(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)




@api_view(['GET'])
def director_detail_view(request, **a):
    if request.method == 'GET':
        director = Director.objects.get(id=a['id'])

        serializer = DirectorSerializer(director, many=False)
        return Response(data=serializer.data, status=HTTP_200_OK)

@api_view(['GET'])
def reviews_views(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)

@api_view(['GET'])
def review_detail_view(request, **a):
    if request.method == 'GET':
        review = Review.objects.get(id=a['id'])

        serializer = ReviewSerializer(review, many=False)
        return Response(data=serializer.data, status=HTTP_200_OK)