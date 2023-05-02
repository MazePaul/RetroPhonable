from django.urls import path

from . import views

urlpatterns = [
    path("", views.GameListView, name="gamelist"),
    path("<int:pk>", views.GameDetailView, name="gamedetails"),
]