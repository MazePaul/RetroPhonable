from django.urls import path

from . import views

urlpatterns = [
    path("", views.GameListView, name="gamelist"),
    path("<int:game_id>", views.GameDetailView, name="gamedetails"),
]