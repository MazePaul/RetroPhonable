from django.urls import path
from . import views
from .views import CategorySearch

app_name='library'

urlpatterns = [
    path("", views.GameListView, name="gamelist"),
    path('search/', CategorySearch, name='CategorySearch'),
    path("game/<int:pk>/", views.GameDetailView, name="GameDetailView"),
]