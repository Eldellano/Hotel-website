from django import template
from django.template.defaultfilters import stringfilter
from typing import Sequence


register = template.Library()


@register.filter(name='cut')
@stringfilter
def cut(value: str) -> str:
    """Для обрезки 'core' у src картинки"""
    return value[4:]


@register.filter(name='range')
def filter_range(number: int) -> Sequence:
    """Для построения последовательности на основе длины объекта"""
    return range(number)
