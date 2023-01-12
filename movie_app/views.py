from rest_framework.response import Response
from rest_framework.decorators import api_view


import movie_app.serializers
from movie_app.models import Movie, Director, Review
from movie_app.serializers import MovieSerializer, DirectorSerializer, ReviewSerializer, \
MovieReviewSerializer, MovieCreateSerializer, DirectorCreateSerializer, ReviewCreateSerializer
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
#hw6

class MovieCreateListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination

class MovieItemUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'

class DirectorCreateListAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination

class DirectorItemUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'

class ReviewModelViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
class MovieReviewListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieReviewSerializer
    pagination_class = PageNumberPagination


@api_view(['GET', 'POST'])
def movies_show_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = MovieCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=HTTP_400_BAD_REQUEST)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')
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
        serializer = MovieCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=HTTP_400_BAD_REQUEST)
        movie.title = serializer.validated_data.get('title')
        movie.description = serializer.validated_data.get('description')
        movie.duration = serializer.validated_data.get('duration')
        movie.director_id = serializer.validated_data.get('director_id')
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
        serializer = DirectorCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=HTTP_400_BAD_REQUEST)
        name = serializer.validated_data.get('name')
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
        serializer = DirectorCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=HTTP_400_BAD_REQUEST)
        director.name = serializer.validated_data.get('name')
        director.save()
        return Response(data={'message': 'sucsess',
                              'director': DirectorSerializer(director).data})


@api_view(['GET', "POST"])
def reviews_views(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ReviewCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=HTTP_400_BAD_REQUEST)
        text = serializer.validated_data.get('text')
        movie_id = serializer.validated_data.get('movie_id')
        stars = serializer.validated_data.get('stars')
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
        serializer = ReviewCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=HTTP_400_BAD_REQUEST)
        review.title =  serializer.validated_data.get('title')
        review.description = serializer.validated_data.get('description')
        review.duration = serializer.validated_data.get('duration')
        review.director_id = serializer.validated_data.get('director_id')
        review.save()
        return Response(data={'message': 'sucsess',
                              'review': ReviewSerializer(review).data})

@api_view(['GET'])
def movies_review_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieReviewSerializer(movies, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)