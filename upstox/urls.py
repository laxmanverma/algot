from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    url(r'^auth/$', views.authorize),
    url(r'^historical/$', views.historical_data),
    url(r'^intraday/$', views.intraday_data)
]
