from django.urls import path
from appmini.views import *
from appmini import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("bikes/", views.bike_list, name="bike_list"),
]