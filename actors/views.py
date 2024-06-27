from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from actors.models import Actor
from .serializers import ActorSerializer


# Create your views here.

class ActorListCreateView(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
