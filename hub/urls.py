from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from EsportHub.settings import MEDIA_ROOT
from hub import views
from hub.views import ImageDisplay, Image

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('list/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('image/', Image.as_view(), name='image'),
    path('image/<int:pk>/', ImageDisplay.as_view(), name='image_display'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('terms/', views.terms, name='terms'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('games/', views.games, name='games'),
    path('snapshots/', views.snapshots, name='snapshots'),
    path('deck-entries/', views.deck_entries, name='deck-entries'),
    path('decks/', views.decks, name='decks'),
    path('cards/', views.cards, name='cards'),
    path('card-versions/', views.card_versions, name='card-versions'),
    path('teams/', views.teams, name='teams'),
    path('players/', views.players, name='players'),
    path('matches/', views.matches, name='matches'),
    path('tournaments/', views.tournaments, name='tournaments'),
    path('streams/', views.streams, name='streams'),
    path('streamers/', views.streamers, name='streamers'),
    path('platforms/', views.platforms, name='platforms')

]