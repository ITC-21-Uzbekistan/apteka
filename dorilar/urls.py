from django.urls import path
from .views import nakladnoy, deletePrixod, add_dori, glavni, postavshik, deleteNakladnoy, create_dori
from .views import pereotsenka, newPereotsenka, search_tovars
from .views import spisaniya, new_spisaniya
from .views import otchoti


urlpatterns = [
    path('', glavni),
    path('prixod/', nakladnoy, name='prixod'),
    path('prixod/<int:id>/', nakladnoy, name='prixodlar_detail'),
    path('add_prixod/<int:id>/', add_dori, name="add_prixod"),
    path('create_dori/', create_dori, name="create_dori"),
    path('nakladnoy_delete/<int:id>/', deleteNakladnoy, name="deleteNakladnoy"),
    path('prixod/delete/<int:idd>', deletePrixod, name="deleteprixod"),
    path('prixod/firma/', postavshik, name="firma"),

    path('pereotsenka/', pereotsenka, name='pereotsenka'),
    path('pereotsenka/<int:id>', newPereotsenka, name="perotsenka_detail"),
    path('search/', search_tovars, name="search"),

    path('spisaniya/', spisaniya, name='spisaniya'),
    path('spisaniya/<int:id>', new_spisaniya, name='new_spisaniya'),
    path('otchoti/', otchoti, name='otchoti'),
]