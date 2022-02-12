from django.urls import path
from .views import nakladnoy, deletePrixod, add_dori, glavni, postavshik, deleteNakladnoy, create_dori
from .views import pereotsenka
from .views import spisaniya
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
    path('spisaniya/', spisaniya, name='spisaniya'),
    path('otchoti/', otchoti, name='otchoti'),
]