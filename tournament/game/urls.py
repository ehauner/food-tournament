from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registration/?', views.registration, name='registration'),
    url(r'^upload/?', views.upload, name='upload'),
    # url(r'^rules/(?P<first>[-\w]+)/$', views.rules, name='rules'),
    url(r'^rules$', views.rules, name='rules'),
    url(r'^match/?', views.match, name='match'),
    url(r'^champion/?', views.champion, name='champion'),
]
