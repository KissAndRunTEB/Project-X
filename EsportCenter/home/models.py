from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(HomePage, self).get_context(request)

        #blogpages=self.get_children()[0].get_children().live()
        blogpages = Page.objects.get(slug='blog')
        blogpages = blogpages.get_children().live().order_by('-last_published_at')
        context['blogpages'] = blogpages

        # Retrieve the "Page Sliders" page dynamically
        slider = Page.objects.get(slug='slides')
        slider = slider.get_children().live().order_by('-last_published_at')

        context['slider'] = slider

        #videos=self.get_children()[3].get_children().live()
        videos = Page.objects.get(slug='videos')
        videos = videos.get_children().live().order_by('-last_published_at')
        context['videos'] = videos
        return context