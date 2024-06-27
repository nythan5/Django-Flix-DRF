from .views import ActorRetrieveUpdateDestroyView, ActorListCreateView
from django.urls import path


urlpatterns = [
    path('', ActorListCreateView.as_view(), name='list_create'),
    path('<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(),
         name='retrieve_update_destroy')

]
