from django.urls import path

from kassa.views import main, table, get_shtrixkod, make_pay

urlpatterns = [
    path('', main, name="home"),
    path('getshtrix/', get_shtrixkod, name="getShtrix"),
    path('make_pay/', make_pay, name="make_pay"),
]
