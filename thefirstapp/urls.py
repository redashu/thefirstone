__author__ = 'ccaf'

from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$',views.default_return),
    url(r'(?P<pk>\d+)/$',views.user_view)
]
