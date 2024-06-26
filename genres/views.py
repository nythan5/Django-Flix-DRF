from .models import Genre
from rest_framework.generics import ListCreateAPIView
from .serializer import GenreSerializer
# Create your views here.


class GenreCreateListView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
