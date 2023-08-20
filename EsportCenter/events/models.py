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



@register_snippet
class EventsCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'events categories'


class EventsTagIndexPage(Page):

    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('tag')
        eventspages = EventsPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['eventspages'] = eventspages
        return context


class EventsIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)

        category_obj = EventsCategory.objects.get(name="Featured")

        eventspages = self.get_children().live().order_by('first_published_at')
        # - sign, gives opposite direction
        #eventspages = self.get_children().live().order_by('-first_published_at')
        context['eventspages'] = eventspages


        # featured = self.get_children().live().order_by('-first_published_at')
        # context['featured'] = featured
        return context


class EventsPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'EventsPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class EventsPage(Page):
    page_description = "Admin panel helpfull tip"

    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=EventsPageTag, blank=True)
    categories = ParentalManyToManyField('events.EventsCategory', blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Events information"),
        FieldPanel('intro'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class EventsPageGalleryImage(Orderable):
    page = ParentalKey(EventsPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]
