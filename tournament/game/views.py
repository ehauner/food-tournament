from __future__ import division
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from game.models import *
from game.forms import DocumentForm
from game import engine
import random

# Clear the database and files
def clear():
    documents = Document.objects.all()
    for document in documents:
        document.delete()
    items = Item.objects.all()
    for item in items:
        item.delete()
    tournaments = Tournament.objects.all()
    for tournament in tournaments:
        tournament.delete()

# Reset the seen tags on items
def reset_seen():
    for item in Item.objects.all():
        item.seen = False
        item.save()

def clear_tournament():
    tournaments = Tournament.objects.all()
    for tournament in tournaments:
        tournament.delete()

# Get a random unseen item
def get_random_unseen_item(filters):
    items = Item.objects.filter(seen=False)
    for this_filter in filters: # filter items with user suggested filters
        items = eval('items.filter(' + this_filter + '=True)')
    if len(items) > 0:
        return items.order_by('?')[0]
    else:
        return None

def index(request):
    return HttpResponse("Hello, world. You're at the game index.")


def registration(request):
    context = {}
    docfile=Document.objects.all().reverse()[0] # Get last uploaded file
    if not len(Item.objects.all()) > 0:
        engine.populate_database(docfile.docfile) # populate database
    context['items'] = Item.objects.all()
    return render(request, 'game/registration.html', context)
    # return HttpResponseRedirect(reverse("game.views.rules"))

def upload(request):
    # Handle file upload
    if request.method == 'POST':
        clear()
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document upload after POST
            return HttpResponseRedirect(reverse("game.views.registration"))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the upload page
    documents = Document.objects.all()

    # Render upload page with the documents and the form
    return render(request, 'game/upload.html', {'documents': documents, 'form': form})

def rules(request):
    context = {}
    if request.method == 'GET':
        context["first"] = Item.objects.get(name=request.GET.get('first'))
    context['items'] = Item.objects.all()
    return render(request, 'game/rules.html', context)

def match(request):
    # Get arguments from url
    if request.method == 'GET':
        left = request.GET.get('left')
        right = request.GET.get('right')
        winner = request.GET.get('winner')
        stats = request.GET.getlist('stats')
        filters = request.GET.getlist('filters')
        first_match = request.GET.get('first_match')
        num_matches = request.GET.get('num_matches')
        current_match = request.GET.get('current_match')

    if first_match is not None: # must set up if this is the first match
        reset_seen() # reset the seen items
        clear_tournament() # remove old tournament
        t = Tournament(num_matches=int(num_matches)) # make new Tournament
        num_matches = t.num_matches
        current_match = 1
        t.save()
    else: # else increment tournament current_match
        t = Tournament.objects.all()[0]
        num_matches = t.num_matches
        t.save()

    # Record if left won
    left_won = winner == left

    # Remember these have been seen
    if left is not None:
        left = Item.objects.get(name=left)
        left.seen = True
        left.save()
    if right is not None:
        right = Item.objects.get(name=right)
        right.seen = True
        right.save()

    # if we have done enough matches
    if int(current_match) > num_matches:
        champion = left if left_won else right
        context = {"champion": champion, "message": "Finished " + str(num_matches) + " matches"}
        return render(request, 'game/champion.html', context)

    # Replace loser
    if left_won:
        right = get_random_unseen_item(filters)
    else:
        left = get_random_unseen_item(filters)

    # if either right or left are none, we have run out of items and we have a champion
    if left is None or right is None:
        champion = left if right is None else right
        context = {"champion": champion, "message": "Ran out of items"}
        return render(request, 'game/champion.html', context)

    # Make dictionaries to hold the items attributes of interest
    left_dict = {}
    for stat in stats:
        left_dict[stat] = eval('left.' + stat)
    right_dict = {}
    for stat in stats:
        right_dict[stat] = eval('right.' + stat)

    # Prepare string for stats and filters
    stats_url_string = ""
    for stat in stats:
        stats_url_string += '&stats=' + stat
    filters_url_string = ""
    for this_filter in filters:
        filters_url_string += '&filters=' + this_filter

    context = {'left_winning_percentage': round(left.matches_won / left.matches_played, 2), 'right_winning_percentage': round(right.matches_won / right.matches_played, 2), 'current_match': current_match, 'next_match': int(current_match) + 1, 'left_won': left_won, 'left':left, 'left_dict': left_dict, 'right': right, 'right_dict': right_dict, 'filters': filters, 'stats': stats, 'stats_url_string': stats_url_string, 'filters_url_string': filters_url_string}
    return render(request, 'game/match.html', context)

def champion(request):
    context = {}
    return render(request, 'game/champion.html', context)
