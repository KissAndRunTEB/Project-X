from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView, TemplateView

from hub.forms import PostForm
from hub.models import Post, MenuItem, Video, Game, Snapshot, DeckEntry, CardVersion, Team, Tournament, Player, Match, \
    Stream, Streamer, Platform


# Images
class Image(TemplateView):
    form = PostForm
    template_name = 'blog/image.html'

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()

            return HttpResponseRedirect(reverse_lazy('image_display', kwargs={'pk': obj.id}))

        context = self.get_context_data(form=form)
        return self.render_to_responce(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ImageDisplay(DetailView):
    model = Post
    template_name = 'blog/image_display.html'
    context_object_name = 'image'


def index(request):
    posts = Post.objects.all().order_by('-publish_date')
    menu = MenuItem.objects.all().order_by('-order')
    user_name = request.user.get_username()
    videos = Video.objects.all().order_by('-publish_date')

    return render(request, 'main/index.html', {'posts': posts, 'menu': menu, 'user_name': user_name, 'videos': videos})


def blog(request):
    posts = Post.objects.all().order_by('-publish_date')
    menu = MenuItem.objects.all().order_by('-order')

    return render(request, 'main/blog.html', {'posts': posts, 'menu': menu})


def games(request):
    games_list = Game.objects.all().order_by('-publish_date')
    menu = MenuItem.objects.all().order_by('-order')

    return render(request, 'lists/games.html', {'games': games_list, 'menu': menu})


def snapshots(request):
    snapshot_list = Snapshot.objects.all().order_by('-publish_date')
    menu = MenuItem.objects.all().order_by('-order')

    return render(request, 'lists/snapshots.html', {'snapshots': snapshot_list, 'menu': menu})


def deck_entries(request):
    deck_entry_list = DeckEntry.objects.all().order_by('-publish_date')
    menu = MenuItem.objects.all().order_by('-order')

    return render(request, 'lists/deck-entries.html', {'deck_entries': deck_entry_list, 'menu': menu})


def decks(request):
    decks_list = DeckEntry.objects.all().order_by('-publish_date')
    menu = MenuItem.objects.all().order_by('-order')

    return render(request, 'lists/decks.html', {'decks': decks_list, 'menu': menu})


def cards(request):
    cards_list = DeckEntry.objects.all().order_by('-publish_date')
    menu = MenuItem.objects.all().order_by('-order')

    return render(request, 'lists/cards.html', {'cards': cards_list, 'menu': menu})


def card_versions(request):
    card_versions_list = CardVersion.objects.all().order_by('-publish_date')
    menu = MenuItem.objects.all().order_by('-order')

    return render(request, 'lists/card-versions.html', {'card_versions': card_versions_list, 'menu': menu})


def teams(request):
    team_list = Team.objects.all().order_by('-publish_date')
    menu = MenuItem.objects.all().order_by('-order')

    return render(request, 'lists/teams.html', {'teams': team_list, 'menu': menu})


def players(request):
    players_list = Player.objects.all().order_by('-publish_date')
    menu = MenuItem.objects.all().order_by('-order')

    return render(request, 'lists/players.html', {'players': players_list, 'menu': menu})


def tournaments(request):
    tournaments_list = Tournament.objects.all().order_by('-publish_date')
    menu = MenuItem.objects.all().order_by('-order')

    return render(request, 'lists/tournaments.html', {'tournaments': tournaments_list, 'menu': menu})


def matches(request):
    matches_list = Match.objects.all().order_by('-publish_date')
    menu = MenuItem.objects.all().order_by('-order')

    return render(request, 'lists/matches.html', {'matches': matches_list, 'menu': menu})


def streams(request):
    stream_list = Stream.objects.all().order_by('-publish_date')
    menu = MenuItem.objects.all().order_by('-order')

    return render(request, 'lists/streams.html', {'streams': stream_list, 'menu': menu})


def streamers(request):
    streamer_list = Streamer.objects.all().order_by('-publish_date')
    menu = MenuItem.objects.all().order_by('-order')

    return render(request, 'lists/streamers.html', {'streamers': streamer_list, 'menu': menu})


def platforms(request):
    platform_list = Platform.objects.all().order_by('-publish_date')
    menu = MenuItem.objects.all().order_by('-order')

    return render(request, 'lists/platforms.html', {'platforms': platform_list, 'menu': menu})


def terms(request):
    posts = Post.objects.all().order_by('-publish_date')

    return render(request, 'other-pages/terms.html', {'posts': posts})


def privacy_policy(request):
    posts = Post.objects.all().order_by('-publish_date')

    return render(request, 'other-pages/privacy-policy.html', {'posts': posts})


# Posts
def post_list(request):
    posts = Post.objects.all().order_by('-publish_date')

    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post})


def error_404_view(request, exception):
    data = {"name": 'Blog error page'}
    return render(request, 'blog/404.html', data, status=404)


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
