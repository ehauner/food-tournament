from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from django.utils.encoding import python_2_unicode_compatible
import os
from django.conf import settings
import random

# Create your models here.

@python_2_unicode_compatible  # only if you need to support Python 2
class Item(models.Model):

    # General
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=200)
    group = models.CharField(max_length=200)

    # Has it been seen in the match?
    seen = models.BooleanField(default = False)

    # Matches
    matches_played = models.IntegerField(default=0)
    matches_won = models.IntegerField(default=0)

    # Price
    price_per_serving = models.IntegerField(default=0)
    serving_size = models.IntegerField(default=0)

    # Nutritional attributes
    calories = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    cholesterol = models.IntegerField(default=0)
    sodium = models.IntegerField(default=0)
    carbohydrates = models.IntegerField(default=0)
    sugar = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    vitA = models.IntegerField(default=0)
    vitC = models.IntegerField(default=0)
    calcium = models.IntegerField(default=0)
    iron = models.IntegerField(default=0)
    fiber = models.IntegerField(default=0)

    # Filters
    vegetarian = models.BooleanField(default = False)
    vegan = models.BooleanField(default = False)
    organic = models.BooleanField(default = False)
    gluten_free = models.BooleanField(default = False)
    nut_free = models.BooleanField(default = False)
    lactose_free = models.BooleanField(default = False)

    def __str__(self):
        return self.name

@python_2_unicode_compatible  # only if you need to support Python 2
class Tournament(models.Model):

    num_matches = models.IntegerField(default=0)
    current_match = models.IntegerField(default=1)

    def __str__(self):
        return self.name

# The following model is for the file upload form
class Document(models.Model):
    docfile = models.FileField(upload_to="files/")
    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.docfile.name))
        super(Document, self).delete(*args, **kwargs)
