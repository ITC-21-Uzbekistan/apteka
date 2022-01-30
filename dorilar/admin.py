from django.contrib import admin
from .models import Tovar, TipTovara, Firma, Nakladnoy, NakladnoyNo


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
        'olingan_narxi',
        'ustiga_foiz',
        'sotiladigan_narx',
        'max_sena',
    ]


class NakladnoyNoAdmin(admin.ModelAdmin):
    list_display = ['nakladnoy_nom', 'postavshik', 'date']


admin.site.register(TipTovara, TipTovaraAdmin)
admin.site.register(Tovar, TovarAdmin)
admin.site.register(Firma, FirmaAdmin)
admin.site.register(NakladnoyNo, NakladnoyNoAdmin)
admin.site.register(Nakladnoy, NakladnoyAdmin)