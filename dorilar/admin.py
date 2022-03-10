from django.contrib import admin
from .models import Tovar, TipTovara, Firma, Nakladnoy, NakladnoyNo, Pereotsenka


class TovarAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'shtrixKod', 'name',
        'tip_tovara', 'shtukPachke',
    ]


class TipTovaraAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'tip',
    ]


class FirmaAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'firma',
    ]


class NakladnoyAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nakladnoy',
        'tovar',
        'olingan_soni',
        'ishlab_chiqaruvchi',
        'dori_sertifikati',
        'srok',
        'date_dobavlen',
        'olingan_narxi',
        'ustiga_foiz',
        'sotiladigan_narx',
        'max_sena',
    ]


class NakladnoyNoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nakladnoy_nom', 'postavshik', 'date']


class PereotsenkaAdmin(admin.ModelAdmin):
    list_display = ['id', 'tovar_id', 'eski_protsent', 'eski_narx', 'yengi_foiz', 'yengi_narx', 'changed_time']


admin.site.register(TipTovara, TipTovaraAdmin)
admin.site.register(Tovar, TovarAdmin)
admin.site.register(Firma, FirmaAdmin)
admin.site.register(NakladnoyNo, NakladnoyNoAdmin)
admin.site.register(Nakladnoy, NakladnoyAdmin)
admin.site.register(Pereotsenka, PereotsenkaAdmin)