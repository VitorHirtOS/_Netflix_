from django.urls import path
from .views import Home, HomeFilmes, DetalhesFilmes

app_name = 'filme'

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('filmes/', HomeFilmes.as_view(), name="homefilmes"),
    path('filmes/<int:pk>', DetalhesFilmes.as_view(), name="detalhesfilme"),
]