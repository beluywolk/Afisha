from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    @property
    def movies_count(self):
        return self.movies.all().count()

class Movie(models.Model):
    title = models.CharField(max_length=90)
    description = models.TextField()
    duration = models.IntegerField(default=120)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title
    @property
    def rating(self):
        count = self.reviews.all().count()
        stars = sum([i.stars for i in self.reviews.all()])
        return stars // count

class Review(models.Model):
    NUMBERS_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name='reviews')
    stars = models.IntegerField(choices=NUMBERS_CHOICES)


