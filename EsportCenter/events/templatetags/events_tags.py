from django import template

from events.models import EventsCategory, EventsPage

register = template.Library()


@register.simple_tag
def events_in_category(category_name):
    # Get the category object
    category_obj = EventsCategory.objects.get(name=category_name)

    # Get all live events in the category
    events = EventsPage.objects.live().filter(categories__in=[category_obj])
    #events = EventsPage.objects.live().order_by('-first_published_at')

    return events
