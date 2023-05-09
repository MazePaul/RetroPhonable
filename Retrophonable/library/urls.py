from django.urls import path
from . import views
from .views import CategorySearch

app_name='library'

urlpatterns = [
    path("", views.GameListView, name="gamelist"),
    path('search/', CategorySearch, name='CategorySearch'),
    path("<int:game_id>", views.GameDetailView, name="gamedetails"),
]