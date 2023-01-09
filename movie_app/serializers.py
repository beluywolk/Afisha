from rest_framework import serializers
from movie_app.models import Movie, Director, Review
from rest_framework.exceptions import ValidationError

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

class MovieCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=90)
    description = serializers.CharField()
    duration = serializers.IntegerField(required=False)
    director_id = serializers.IntegerField(min_value=1)
    def validate_director_id(self, director_id):
        directors = Director.objects.filter(id=director_id)
        if not directors:
            raise ValidationError('i dont know this director')


class DirectorCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)

class ReviewCreateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie_id = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(min_value=1, max_value=5)
    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except:
            raise ValidationError('i dont know this movie')
        return movie_id