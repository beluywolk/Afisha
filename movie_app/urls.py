from django.urls import path
from movie_app.views import movies_show_view, movie_detail_view, directors_views, director_detail_view, \
    reviews_views, review_detail_view, movies_review_view, MovieCreateListAPIView, MovieItemUpdateDeleteAPIView, \
    DirectorCreateListAPIView, ReviewModelViewSet, DirectorItemUpdateDeleteAPIView, MovieReviewListAPIView


urlpatterns = [
    path('movies/', MovieCreateListAPIView.as_view()),
    path('movies/<int:id>/', MovieItemUpdateDeleteAPIView.as_view()),
    path('directors/', DirectorCreateListAPIView.as_view()),
    path('directors/<int:id>/', DirectorItemUpdateDeleteAPIView.as_view()),
    path('reviews/', ReviewModelViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('reviews/<int:id>', ReviewModelViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'

    })),
    path('movies/reviews/', MovieReviewListAPIView.as_view())

]