from django.urls import path
from . import views

app_name = 'genres'

urlpatterns = [
    path('', views.GenreCreateListView.as_view(), name='create_list'),
    # path('<int:pk>/', views.detail_view, name='detail')
]
