from .views import MovieListCreateView, MovieRetrieveUpdateDestroyView, MovieStatsView  # noqa
from django.urls import path

app_name = 'movies'

urlpatterns = [
    path('', MovieListCreateView.as_view(), name='list_create'),
    path('<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(),
         name='retrieve_update_destroy'),
    path('stats/', MovieStatsView.as_view(), name='status')

]
