import string

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
class BlogCategory(models.Model):
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
        verbose_name_plural = 'blog categories'


class BlogTagIndexPage(Page):

    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)

        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages

        category_id = request.GET.get('category')

        if category_id is not None:
            # category = []
            # category.append(BlogCategory.objects.get(id=category_id))
            # context['blogpages'] =  self.get_children().filter(
            #     live=True,
            #     categories=category
            #     categories=category
            # ).order_by('-first_published_at')
            # Filter by tag
            tag = request.GET.get('tag')
            blogpages = BlogPage.objects.filter(live=True, categories=category_id)

            context['blogpages'] = blogpages

        categories = BlogCategory.objects.all()
        context['categories'] = categories

        # start_url_0 = request.build_absolute_uri()
        # context['current_url'] = start_url_0
        #
        # start_url_1 = request.build_absolute_uri()
        # style_value=1
        # if f'style={style_value}' not in start_url_1:
        #     start_url_1 = start_url_1.replace("?style=2&", "?")
        #     start_url_1 = start_url_1.replace("?style=2", "")
        #     start_url_1 = start_url_1.replace("&style=2", "")
        #     if '?' in start_url_1:
        #         start_url_1 += f'&style={style_value}'
        #     else:
        #         start_url_1 += f'?style={style_value}'
        # context['current_url_to_style1'] = start_url_1
        #
        # start_url_2 = request.build_absolute_uri()
        # style_value=2
        # if f'style={style_value}' not in start_url_2:
        #     start_url_2 = start_url_2.replace("?style=1&", "?")
        #     start_url_2 = start_url_2.replace("?style=1", "")
        #     start_url_2 = start_url_2.replace("&style=1", "")
        #     if '?' in start_url_2:
        #         start_url_2 += f'&style={style_value}'
        #     else:
        #         start_url_2 += f'?style={style_value}'
        # context['current_url_to_style2'] = start_url_2


        return context


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class BlogPage(Page):
    page_description = "Admin panel helpfull tip"

    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)

    author = models.CharField(max_length=255, default="Horpyna")

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
        ], heading="Blog information"),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('author'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]
