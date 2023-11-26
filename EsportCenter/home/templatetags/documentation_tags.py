
from django import template

register = template.Library()

@register.simple_tag
def documentation_link():
    return '/static/docs/_build/html/index.html'