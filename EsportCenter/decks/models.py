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


class DecksIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)

        deckspages = self.get_children().live().order_by('-first_published_at')
        context['deckspages'] = deckspages

        return context


class DecksPage(Page):
    page_description = "Adding new Deck"

    date = models.DateField("Post date",default=timezone.now)
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    name = models.CharField(max_length=250)

    stars = models.FloatField(default=3)
    faction = models.CharField(max_length=250, default="")
    link = models.CharField(max_length=250, default="")
    good = models.CharField(max_length=500, default="")
    bad = models.CharField(max_length=500, default="")

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
        ], heading="Deck information"),
        FieldPanel('name'),
        FieldPanel('stars'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('faction'),
        FieldPanel('link'),
        FieldPanel('good'),
        FieldPanel('bad'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class DecksPageGalleryImage(Orderable):
    page = ParentalKey(DecksPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]
