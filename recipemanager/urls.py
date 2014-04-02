from django.conf import settings
from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.main, name='main'),
    url(r'^viewrecipe/(?P<recipeId>\d+)/$', views.viewrecipe, name="viewrecipe")
)
