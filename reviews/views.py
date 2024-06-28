from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView  # noqa
from .models import Review
from .serializers import ReviewSerializer

# Create your views here.


class ReviewListCreateView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
