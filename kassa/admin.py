from django.contrib import admin
from .models import Arxiv


class ArxivAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nakladnoy',
        'tovar_name',
        'tovar_shtrix_kod',
        'tovar_shtuk_pachke',
        'tovar_type',
        'narx',
        'srok',
        'soni',
        'summa',
        'sold',
        'user'
    ]


admin.site.register(Arxiv, ArxivAdmin)