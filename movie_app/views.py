from rest_framework.response import Response
from rest_framework.decorators import api_view


import movie_app.serializers
from movie_app.models import Movie, Director, Review
from movie_app.serializers import MovieSerializer, DirectorSerializer, ReviewSerializer, MovieReviewSerializer
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT


@api_view(['GET', 'POST'])
def movies_show_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        return Response(data={'message': 'sucsess',
                              'movie': MovieSerializer(movie).data})

@api_view(['GET', "PUT", 'DELETE'])
def movie_detail_view(request, **a):
    try:
        movie = Movie.objects.get(id=a['id'])
        data = movie_app.serializers.MovieSerializer(movie).data

    except Movie.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND,
                        data={'message': 'Sorry, we dont have something like that'})

    if request.method == 'GET':
        return Response(data=data, status=HTTP_200_OK)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.save()
        return Response(data={'message': 'sucsess',
                              'movie': MovieSerializer(movie).data})




@api_view(['GET', 'POST'])
def directors_views(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return Response(data={'message': 'sucsess',
                              'director': DirectorSerializer(director).data})




@api_view(['GET', 'PUT', "DELETE"])
def director_detail_view(request, **a):
    try:
        director = Director.objects.get(id=a['id'])
    except:
        return Response(status=HTTP_404_NOT_FOUND,
                        data={'message': 'Sorry, we dont have something like that'})
    if request.method == 'GET':
        serializer = DirectorSerializer(director, many=False)
        return Response(data=serializer.data, status=HTTP_200_OK)
    if request.method == 'DELETE':
        director.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        director.title = request.data.get('title')
        director.description = request.data.get('description')
        director.duration = request.data.get('duration')
        director.director_id = request.data.get('director_id')
        director.save()
        return Response(data={'message': 'sucsess',
                              'movie': MovieSerializer(director).data})


@api_view(['GET', "POST"])
def reviews_views(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')
        review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
        return Response(data={'message': 'sucsess',
                              'review': ReviewSerializer(review).data})
@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, **a):
    try:
        review = Review.objects.get(id=a['id'])
    except:
        return Response(status=HTTP_404_NOT_FOUND,
                        data={'message': 'Sorry, we dont have something like that'})
    if request.method == 'GET':
        serializer = ReviewSerializer(review, many=False)
        return Response(data=serializer.data, status=HTTP_200_OK)

    if request.method == 'DELETE':
        review.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        review.title = request.data.get('title')
        review.description = request.data.get('description')
        review.duration = request.data.get('duration')
        review.director_id = request.data.get('director_id')
        review.save()
        return Response(data={'message': 'sucsess',
                              'movie': MovieSerializer(review).data})

@api_view(['GET'])
def movies_review_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieReviewSerializer(movies, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)