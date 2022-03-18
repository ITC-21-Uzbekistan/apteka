from django.urls import path

from kassa.views import main, table

urlpatterns = [
    path('', main, name="home"),
    path('table/', table, name="table")
]