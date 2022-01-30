from django.urls import path
from .views import prixod, deletePrixod, prixod_detail, glavni
from .views import pereotsenka
from .views import spisaniya
from .views import otchoti


urlpatterns = [
    path('', glavni),
    path('prixod/', prixod, name='prixod'),
    path('prixod/<int:id>/', prixod, name='prixodlar_detail'),
    path('prixod_detail/<int:id>/', prixod_detail, name="prixod_detail"),
    path('prixod/delete/<int:idd>', deletePrixod, name="deleteprixod"),

    path('pereotsenka/', pereotsenka, name='pereotsenka'),
    path('spisaniya/', spisaniya, name='spisaniya'),
    path('otchoti/', otchoti, name='otchoti'),
]