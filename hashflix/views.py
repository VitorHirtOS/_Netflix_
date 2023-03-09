from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView

# Functions Class Base Views -> Sites complexos, tendo templates prontos OU Functions Class View -> Sites simples, não vem com templates prontos

# Create your views here.
# def Home(request):
#    return render(request, 'hashflix/pages/home.html')


class Home(TemplateView):
    template_name = 'hashflix/pages/home.html'
 

# def HomeFilme(request):
#    context = {}
#    lista_filmes = Filme.objects.all()
#    context['lista_filmes'] = lista_filmes
#    return render(request, 'hashflix/pages/homefilmes2.html', context)

class HomeFilmes(ListView):
    template_name = 'hashflix/pages/homefilmes2.html'
    model = Filme # object.list

class DetalhesFilmes(DetailView):
    template_name = 'hashflix/pages/detalhesfilmes.html'
    model = Filme