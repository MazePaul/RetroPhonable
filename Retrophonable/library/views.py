from django.shortcuts import get_object_or_404, render
from django.contrib import messages
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

def CategorySearch(request):
    if request.method == "POST":
        search_query = request.POST.get('search_query', '')
        #enumeration des différentes catégories possible
        cat_console = request.POST.get('console', '')
        cat_category = request.POST.get('category', '')
        cat_multiplayer = request.POST.get('multiplayer', '')
        #in case of console and category left empty
        games = Game.objects.all()

        if search_query:
            games = games.filter(title_text__icontains=search_query)
        if cat_console:
            games = games.filter(console_text=cat_console)
        if cat_category:
            games = games.filter(category_text=cat_category)
        if cat_multiplayer:
            games = games.filter(multiplayer=cat_multiplayer)
        context = {
            "games": games
        }
        return render(request, 'library/index.html', context)