from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter(name='cut')
@stringfilter
def cut(value):
    """Для обрезки 'core' у src картинки"""
    return value[4:]
