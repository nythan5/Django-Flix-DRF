from django.urls import path
from .views import ReviewListCreateView, ReviewRetrieveUpdateDestroyView

app_name = 'reviews'

urlpatterns = [
    path('api/', ReviewListCreateView.as_view(), name='list_create'),
    path('api/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(),
         name='retrieve_update_destroy')
]
