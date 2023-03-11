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
class VideosCategory(models.Model):
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
        verbose_name_plural = 'videos categories'


class VideosTagIndexPage(Page):

    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('tag')
        videospages = VideosPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['videospages'] = videospages
        return context


class VideosIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        videospages = self.get_children().live().order_by('-first_published_at')
        context['videospages'] = videospages
        return context


class VideosPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'VideosPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class VideosPage(Page):
    page_description = "Admin panel helpfull tip"

    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    link = models.CharField(max_length=500)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=VideosPageTag, blank=True)
    categories = ParentalManyToManyField('videos.VideosCategory', blank=True)

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
        ], heading="Videos information"),
        FieldPanel('intro'),
        FieldPanel('link'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class VideosPageGalleryImage(Orderable):
    page = ParentalKey(VideosPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]
