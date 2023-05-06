from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from .models import Game

def GameListView(request):
    #appel API pour lister l'ensemble des jeux vidéosw
    games = Game.objects.order_by("title_text")

    if request.method == "POST":
        if request.name == "categorie":
            games = Game.object.order_by("categorie_text")

    # The context is a dictionary mapping template variable names to Python objects.
    # le mot clé "games" va permettre à l'index.html de faire le lien avec la variable games d'ici
    context = {"games": games}
    # It’s a very common idiom to load a template, fill a context and return an HttpResponse object with the result of the rendered template.
    return render(request, "library/index.html", context)


def GameDetailView(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, "library/detail.html", {"game":game})

def ButtonSearch(request):
    if request.method == "POST":
        #if "recherche" in request.POST:
        search_query = request.POST.get('search_query', '')
        games = Game.objects.filter(title_text__icontains=search_query)
        context = {"games": games, "search_query": search_query}
        return render(request, 'library/index.html', context)