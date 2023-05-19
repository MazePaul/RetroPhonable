from django.urls import path
from . import views
from .views import CategorySearch
from django.conf.urls.static import static
from django.conf import settings

app_name='library'

urlpatterns = [
    path("", views.GameListView, name="gamelist"),
    path('search/', CategorySearch, name='CategorySearch'),
    path("search/<int:pk>/", views.GameDetailView, name="GameDetailView"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)