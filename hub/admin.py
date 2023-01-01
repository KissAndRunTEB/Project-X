from django.contrib import admin

from hub.models import Post, MenuItem, Video, FastNews, Game, Snapshot, DeckEntry, Deck, Card, CardVersion, Tournament, Player, PlayerTournamentEntry, Team, Match, Stream, Streamer, Platform

# Register your models here.


admin.site.register(Post)

admin.site.register(FastNews)

admin.site.register(Video)

admin.site.register(MenuItem)

admin.site.register(Game)

admin.site.register(Snapshot)

admin.site.register(DeckEntry)

admin.site.register(Deck)

admin.site.register(Card)

admin.site.register(CardVersion)

admin.site.register(Tournament)

admin.site.register(Player)

admin.site.register(PlayerTournamentEntry)

admin.site.register(Team)

admin.site.register(Match)

admin.site.register(Streamer)

admin.site.register(Stream)

admin.site.register(Platform)



