from django.urls import path
from movie_app.views import movies_show_view, movie_detail_view, directors_views, director_detail_view, \
    reviews_views, review_detail_view


urlpatterns = [
    path('movies/', movies_show_view),
    path('movies/<int:id>/', movie_detail_view),
    path('directors/', directors_views),
    path('directors/<int:id>/', director_detail_view),
    path('reviews/', reviews_views),
    path('reviews/<int:id>', review_detail_view)

]