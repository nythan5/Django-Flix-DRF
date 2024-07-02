from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView  # noqa
from .models import Movie
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieSerializer

# Create your views here.


class MovieListCreateView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)


class MovieRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)
