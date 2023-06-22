from django import template


register = template.Library()

@register.filter
def sort_by_order(items):
    return sorted(items, key=lambda item: item.specific.order)