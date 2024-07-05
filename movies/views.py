from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView  # noqa
from rest_framework.views import APIView
from .models import Movie
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieSerializer
from project.permissions import GlobalDefaultPermission
from rest_framework import response, status
from django.db.models import Count, Avg
from reviews.models import Review

# Create your views here.


class MovieListCreateView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)


class MovieRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)


class MovieStatsView(APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()

        # A função annotate adiciona agregações aos valores retornados pelo queryset. # noqa
        # Aqui, estamos adicionando uma contagem de IDs (Count('id')) para cada grupo de gêneros. # noqa
        # Basicamente, ele conta quantos filmes existem para cada gênero.
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))  # noqa

        total_reviews = Review.objects.count()

        # Aqui criamos um campo chamado avg_stars que recebe a Media do total de estrelas # noqa
        # atravês da função Avg e posteriormente como pegamos apenas este campo atraves dos [] # noqa
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']  # noqa

        movie_stats = {
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_review': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0
        }

        # Podemos criar um serializer para poder fazer validacoes e calculos caso necessário # noqa
        # Neste caso nao precisa pois já montamos o dicionario na variavel acima. # noqa

        return response.Response(data=movie_stats, status=status.HTTP_200_OK)
