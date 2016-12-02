from django.conf.urls import url
from django.contrib import admin

from booking.views import createbooking
from . import views
urlpatterns = [
    url(r'^createbooking/$', views.createbooking, name="createbooking"),


]
