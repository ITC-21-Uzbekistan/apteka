from django.urls import path

from kassa.views import main, get_shtrixkod, make_pay, authontification, log_out_from_kassa, \
    search_from_arxiv_by_shtrix, search_arxiv, do_vozvrat

urlpatterns = [
    path('', main, name="home"),
    path('login/', authontification),
    path('logout/', log_out_from_kassa, name="logout"),

    path('getshtrix/', get_shtrixkod, name="getShtrix"),
    path('make_pay/', make_pay, name="make_pay"),

    path('searchShtrix/', search_from_arxiv_by_shtrix, name="searchShtrix"),
    path('search/', search_arxiv, name="searchByName"),

    path('doVozvrat/', do_vozvrat, name="do_vozvrat"),
]
