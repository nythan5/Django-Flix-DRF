from django.urls import path
from . import views

app_name = 'genres'

urlpatterns = [
    path('', views.list_view, name='list')
]
