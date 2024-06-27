from .views import MovieListCreateView, MovieRetrieveUpdateDestroyView
from django.urls import path

app_name = 'movies'

urlpatterns = [
    path('', MovieListCreateView.as_view(), name='list_create'),
    path('<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(),
         name='retrieve_update_destroy')

]
