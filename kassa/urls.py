from django.urls import path

from kassa.views import main

urlpatterns = [
    path('', main, name="home")
]