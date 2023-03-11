from django import forms
from django.db import models
from django.db.models import TextField

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.blocks import RawHTMLBlock
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index

from wagtail.snippets.models import register_snippet


class CustomIndexPage(Page):
    page_description = "Admin panel helpfull tip"

    date = models.DateField("Post date")
    header = models.CharField(max_length=250)
    body = TextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        custompages = self.get_children().live().order_by('-first_published_at')
        context['custompages'] = custompages
        return context

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
        ], heading="Custom information"),
        FieldPanel('header'),
        FieldPanel('body'),
    ]