from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


# Create your models here.

class Post(models.Model):
    tags = TaggableManager()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = RichTextField()
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/', default='images/default.jpg')

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Video(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/', default='images/default.jpg')

    def add(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class FastNews(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def add(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True, null=True)
    order = models.IntegerField(default=1)
    location = models.CharField(max_length=200, default="Header")

    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def addItem(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Game(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    logo = models.ImageField(null=True, blank=True, upload_to='images/', default='images/default.jpg')
    image = models.ImageField(null=True, blank=True, upload_to='images/', default='images/default.jpg')
    link_to_website = models.CharField(max_length=200, blank=True, null=True)
    link_to_twitter = models.CharField(max_length=200, blank=True, null=True)
    link_to_facebook = models.CharField(max_length=200, blank=True, null=True)
    link_to_instagram = models.CharField(max_length=200, blank=True, null=True)
    link_to_youtube = models.CharField(max_length=200, blank=True, null=True)
    link_to_twitch = models.CharField(max_length=200, blank=True, null=True)
    link_to_discord = models.CharField(max_length=200, blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Snapshot(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    date = models.DateTimeField(default=timezone.now)
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class DeckEntry(models.Model):
    title = models.CharField(max_length=200)
    ranking = models.IntegerField()
    tier = models.IntegerField()
    link = models.CharField(max_length=200)
    snapshot = models.ForeignKey(Snapshot, on_delete=models.CASCADE)

    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Deck(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Card(models.Model):
    name = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class CardVersion(models.Model):
    name = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    description = RichTextField()
    provision = models.IntegerField()
    power = models.IntegerField()

    game_version = models.CharField(max_length=200)

    date = models.DateTimeField(default=timezone.now)
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Tournament(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    date = models.DateTimeField(default=timezone.now)

    players_limit = models.IntegerField()

    logo = models.ImageField(null=True, blank=True, upload_to='images/', default='images/default.jpg')
    image = models.ImageField(null=True, blank=True, upload_to='images/', default='images/default.jpg')

    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=200)

    logo = models.ImageField(null=True, blank=True, upload_to='images/', default='images/default.jpg')

    link_to_website = models.CharField(max_length=200, blank=True, null=True)
    link_to_twitter = models.CharField(max_length=200, blank=True, null=True)
    link_to_facebook = models.CharField(max_length=200, blank=True, null=True)
    link_to_instagram = models.CharField(max_length=200, blank=True, null=True)
    link_to_youtube = models.CharField(max_length=200, blank=True, null=True)
    link_to_twitch = models.CharField(max_length=200, blank=True, null=True)
    link_to_discord = models.CharField(max_length=200, blank=True, null=True)

    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Player(models.Model):
    nick = models.CharField(max_length=200)
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)

    avatar = models.ImageField(null=True, blank=True, upload_to='images/', default='images/default.jpg')

    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nick


class PlayerTournamentEntry(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    create_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nick


class Match(models.Model):
    playerA = models.ForeignKey(Player, related_name='playerA', on_delete=models.CASCADE)
    playerB = models.ForeignKey(Player, related_name='playerB', on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    scoreA = models.IntegerField()
    scoreB = models.IntegerField()

    state = models.CharField(max_length=200)

    date = models.DateTimeField(default=timezone.now)

    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.playerA + self.playerB


class Streamer(models.Model):
    nick = models.CharField(max_length=200)

    link_to_twitter = models.CharField(max_length=200, blank=True, null=True)
    link_to_facebook = models.CharField(max_length=200, blank=True, null=True)
    link_to_instagram = models.CharField(max_length=200, blank=True, null=True)
    link_to_youtube = models.CharField(max_length=200, blank=True, null=True)
    link_to_twitch = models.CharField(max_length=200, blank=True, null=True)
    link_to_discord = models.CharField(max_length=200, blank=True, null=True)

    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nick


class Platform(models.Model):
    name = models.CharField(max_length=200)

    link = models.CharField(max_length=200, blank=True, null=True)

    logo = models.ImageField(null=True, blank=True, upload_to='images/', default='images/default.jpg')

    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Stream(models.Model):
    title = models.CharField(max_length=200)
    streamer = models.ForeignKey(Streamer, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    date = models.DateTimeField(default=timezone.now)

    howlong = models.IntegerField()

    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
