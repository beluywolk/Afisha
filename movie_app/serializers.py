from rest_framework import serializers
from movie_app.models import Movie, Director, Review




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
    class Meta:
        model = Review
        fields = ('id', 'text', 'stars')

class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Movie
        fields = ('id',  'title', 'reviews', 'rating')

