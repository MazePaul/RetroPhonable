from django.urls import path
from . import views
from .views import ButtonSearch

app_name='library'

urlpatterns = [
    path("", views.GameListView, name="gamelist"),
    path('search/', ButtonSearch, name='ButtonSearch'),
    path("<int:game_id>", views.GameDetailView, name="gamedetails"),
]