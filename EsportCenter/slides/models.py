from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.search import index

from wagtail.snippets.models import register_snippet

from blog.models import BlogPage


# Create your models here.
class SlidesPage(Page):
    OPTIONSFORSTYLE = [
        ('option1', 'News left'),
        ('option2', 'News central'),
        ('option3', 'Special'),
    ]

    page_description = "Add new Slide here"
    date = models.DateField("Post date")

    style = models.CharField(max_length=20, choices=OPTIONSFORSTYLE, default=OPTIONSFORSTYLE[0][0])
    image = models.ImageField(upload_to='sliders')
    text = RichTextField(blank=True)
    secondtext = RichTextField(blank=True)
    thirdtext = RichTextField(blank=True)
    link = models.URLField(blank=True)
    news = models.ForeignKey(
        BlogPage,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # def main_image(self):
    #     gallery_item = self.gallery_images.first()
    #     if gallery_item:
    #         return gallery_item.image
    #     else:
    #         return None

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
        ], heading="Sliders information"),

        FieldPanel('style'),
        FieldPanel('image'),
        FieldPanel('text'),
        FieldPanel('secondtext'),
        FieldPanel('thirdtext'),
        FieldPanel('link'),
        PageChooserPanel('news'),
    ]


class SlidesIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)

        slides = self.get_children().live().order_by('-date')

        context['slides'] = slides

        return context
