from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter(name='cut')
@stringfilter
def cut(value):
    """Removes all values of arg from the given string"""
    return value[4:]
