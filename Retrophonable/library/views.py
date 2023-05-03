from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Game

def GameListView(request):
    #appel API pour lister l'ensemble des jeux vidéos
    games = Game.objects.order_by("title_text")

    # The context is a dictionary mapping template variable names to Python objects.
    # le mot clé "games" va permettre à l'index.html de faire le lien avec la variable games d'ici
    context = {"games": games}
    # It’s a very common idiom to load a template, fill a context and return an HttpResponse object with the result of the rendered template.
    return render(request, "library/index.html", context)


def GameDetailView(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, "library/detail.html", {"game":game})