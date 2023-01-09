from rest_framework import serializers
from movie_app.models import Movie, Director, Review

class MovieNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title')


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name', 'movies_count')

class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director')

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieNameSerializer()
    class Meta:
        model = Review
        fields = ('id', 'movie', 'text', 'stars')

class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Movie
        fields = ('id',  'title', 'reviews', 'rating')

