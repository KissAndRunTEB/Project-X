from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index

from wagtail.snippets.models import register_snippet


# Create your models here.
class StreamersPage(Page):
    page_description = "Add new Streamer here"
    date = models.DateField("Post date")

    nick = models.CharField(max_length=250)
    description = RichTextField(blank=True)
    language = models.CharField(max_length=250)

    TwitchName = models.CharField(max_length=500, null=True, blank=True)
    TwitchLink = models.CharField(max_length=500, null=True, blank=True)
    YoutubeName = models.CharField(max_length=500, null=True, blank=True)
    YoutubeLink = models.CharField(max_length=500, null=True, blank=True)
    TiktokName = models.CharField(max_length=500, null=True, blank=True)
    TiktokLink = models.CharField(max_length=500, null=True, blank=True)
    TwitterName = models.CharField(max_length=500, null=True, blank=True)
    TwitterLink = models.CharField(max_length=500, null=True, blank=True)
    InstagramName = models.CharField(max_length=500, null=True, blank=True)
    InstagramLink = models.CharField(max_length=500, null=True, blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('nick'),
        index.SearchField('description'),
        index.SearchField('language'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
        ], heading="Blog information"),
        FieldPanel('nick'),
        FieldPanel('description'),
        FieldPanel('language'),
        InlinePanel('gallery_images', label="Gallery images"),
        FieldPanel('TwitchName'),
        FieldPanel('TwitchLink'),
        FieldPanel('YoutubeName'),
        FieldPanel('YoutubeLink'),
        FieldPanel('TiktokName'),
        FieldPanel('TiktokLink'),
        FieldPanel('TwitterName'),
        FieldPanel('TwitterLink'),
        FieldPanel('InstagramName'),
        FieldPanel('InstagramLink'),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)

        # streamerspages = self.get_children().live().order_by('-first_published_at')
        # context['streamerspages'] = streamerspages

        from schedules.models import SchedulesPage
        schedule = SchedulesPage.objects.first()  # Retrieve the RelatedClass object
        context['schedule'] = schedule

        return context

class StreamersIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)

        streamerspages = self.get_children().live().order_by('-first_published_at')
        context['streamerspages'] = streamerspages

        from schedules.models import SchedulesPage
        schedule = SchedulesPage.objects.first()  # Retrieve the RelatedClass object
        context['schedule'] = schedule

        return context


class StreamersPageGalleryImage(Orderable):
    page = ParentalKey(StreamersPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]
