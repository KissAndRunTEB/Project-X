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

        blogpages=self.get_children()[0].get_children().live()
        context['blogpages'] = blogpages

        # Retrieve the "Page Sliders" page dynamically
        slider = Page.objects.get(slug='slides')

        # Retrieve the children of the "Page Sliders" page
        slider = slider.get_children().live().order_by('-last_published_at')

        context['slider'] = slider

        videos=self.get_children()[3].get_children().live()
        context['videos'] = videos
        return context