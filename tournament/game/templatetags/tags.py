from django import template
from django.utils.safestring import mark_safe
from django.conf import settings
import re

register = template.Library()

@register.simple_tag
def add_units(value, stat):
    value = str(value)
    if stat == "price_per_serving":
        value = "$" + value
    elif stat == "serving_size":
        value = value + "g"
    elif stat == "calories":
        value = str(int(round(float(value), 0)))
    elif stat == "fat":
        value = value + "g"
    elif stat == "cholesterol":
        value = value + "mg"
    elif stat == "sodium":
        value = value + "mg"
    elif stat == "carbohydrates":
        value = value + "g"
    elif stat == "sugar":
        value = value + "g"
    elif stat == "protein":
        value = value + "g"
    elif stat == "vitA":
        value = value + "%"
    elif stat == "vitC":
        value = value + "%"
    elif stat == "calcium":
        value = value + "%"
    elif stat == "iron":
        value = value + "%"
    elif stat == "fiber":
        value = value + "g"
    elif stat == "serving_size":
        value = value + "g"
    elif stat == "left_winning_percentage":
        value = value + "%"
    elif stat == "right_winning_percentage":
        value = value + "%"
    return mark_safe(value)

@register.filter(name='expand_vitamins')
def expand_vitamins(string):
    if "vit" in string:
        string = string.replace("vit", "vitamin ")
    return mark_safe(string)
