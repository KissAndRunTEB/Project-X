from django import forms
from django.db import models
from django.utils import timezone

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index

from wagtail.snippets.models import register_snippet

from games.models import GamesPage

class SnapshotsIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)

        snapshotspages = self.get_children().live().order_by('-first_published_at')
        context['snapshotspages'] = snapshotspages

        return context


class SnapshotsPage(Page):
    page_description = "Adding new Snapshot"

    date = models.DateField("Post date",default=timezone.now)
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    name = models.CharField(max_length=250)
    game = models.ForeignKey(
        GamesPage,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='snapshots'
    )

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('name'),
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
        ], heading="Snapshot information"),
        FieldPanel('name'),
        FieldPanel('intro'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
        FieldPanel('game'),
    ]


    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)

        # streamerspages = self.get_children().live().order_by('-first_published_at')
        # context['streamerspages'] = streamerspages

        #from games.models import GamesPage
        games = GamesPage.objects.first()  # Retrieve the RelatedClass object
        context['game'] = games

        return context


class SnapshotsPageGalleryImage(Orderable):
    page = ParentalKey(SnapshotsPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]
