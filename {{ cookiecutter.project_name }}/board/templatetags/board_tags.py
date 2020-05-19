from bson import json_util

from django import template

register = template.Library()


@register.filter(name='get')
def func_get(obj, key):
    return obj[key]
