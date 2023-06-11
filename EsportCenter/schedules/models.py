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

from streamers.models import StreamersPage


# Create your models here.
class SchedulesPage(Page):
    page_description = "Add new Schedule here"
    date = models.DateField("Post date")

    streamer= models.OneToOneField(
        StreamersPage,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='my_page'
    )

    nick = models.CharField(max_length=250)
    timezone = models.CharField(max_length=250, null=True)

    isMonday = models.BooleanField(default=False)
    hourMonday = models.CharField(max_length=250, null=True, blank=True)

    isTuesday = models.BooleanField(default=False)
    hourTuesday = models.CharField(max_length=250, null=True, blank=True)

    isWednesday = models.BooleanField(default=False)
    hourWednesday = models.CharField(max_length=250, null=True, blank=True)

    isThursday = models.BooleanField(default=False)
    hourThursday = models.CharField(max_length=250, null=True, blank=True)

    isFriday = models.BooleanField(default=False)
    hourFriday = models.CharField(max_length=250, null=True, blank=True)

    isSaturday = models.BooleanField(default=False)
    hourSaturday = models.CharField(max_length=250, null=True, blank=True)

    isSunday = models.BooleanField(default=False)
    hourSunday = models.CharField(max_length=250, null=True, blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('nick'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
        ], heading="Schedules information"),

        FieldPanel('streamer'),

        FieldPanel('nick'),
        FieldPanel('timezone'),

        FieldPanel('isMonday'),
        FieldPanel('hourMonday'),
        FieldPanel('isTuesday'),
        FieldPanel('hourTuesday'),
        FieldPanel('isWednesday'),
        FieldPanel('hourWednesday'),
        FieldPanel('isThursday'),
        FieldPanel('hourThursday'),
        FieldPanel('isFriday'),
        FieldPanel('hourFriday'),
        FieldPanel('isSaturday'),
        FieldPanel('hourSaturday'),
        FieldPanel('isSunday'),
        FieldPanel('hourSunday'),

        InlinePanel('gallery_images', label="Gallery images"),
    ]


class SchedulesIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)

        schedulespages = self.get_children().live().order_by('-first_published_at')
        context['schedulespages'] = schedulespages

        return context


class SchedulesPageGalleryImage(Orderable):
    page = ParentalKey(SchedulesPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]
