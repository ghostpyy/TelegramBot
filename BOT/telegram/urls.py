from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'telegram/$', telegram),
    url(r'friends/$', friends, name='friends'),
    url(r'friends/increase/(?P<pk>\d+)/', icount, name='icount'),
    url(r'add/friend/$', addfriend, name='addfriend'),
    url(r'friends/json/$',jsonfriends)
]
