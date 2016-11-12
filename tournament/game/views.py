from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from game.models import *
from game.forms import DocumentForm
from game import engine

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
        context["first"] = request.GET.get('first')
    context['items'] = Item.objects.all()
    return render(request, 'game/rules.html', context)

def match(request):
    context = {}
    if request.method == 'GET':
        context["first"] = request.GET.get('first')
    context['items'] = Item.objects.all()
    return render(request, 'game/match.html', context)

def champion(request):
    context = {}
    return render(request, 'game/champion.html', context)
