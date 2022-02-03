from django import forms
from .models import Tovar, TipTovara, Firma, Nakladnoy, NakladnoyNo


class TovarForm(forms.ModelForm):

    class Meta:
        model = Tovar
        fields = ('shtrixKod', 'name',
                  'tip_tovara', 'shtukPachke',
                  )

        labels = {
            'shtrixKod': 'Штрих-код лекарства',
            'name': 'Название лекарства',
            'tip_tovara': 'Тип препарата',
            'shtukPachke': 'Количество в одну пачеке',
        }


class TipTovaraForm(forms.ModelForm):

    class Meta:
        model = TipTovara
        fields = ('tip',)

        labels = {
            'tip': 'Тип Товара',
        }


class FirmaForm(forms.ModelForm):

    class Meta:
        model = Firma
        fields = ('firma',)

        labels = {
            'firma': 'Поставшик',
        }


class NakladnoyNoForm(forms.ModelForm):

    class Meta:
        model = NakladnoyNo
        fields = ('nakladnoy_nom', 'postavshik')


class NakladnoyForm(forms.ModelForm):

    class Meta:
        model = Nakladnoy
        fields = ('id', 'nakladnoy',
                  'tovar', 'olingan_soni',
                  'ishlab_chiqaruvchi', 'dori_sertifikati',
                  'olingan_narxi', 'ustiga_foiz',
                  'sotiladigan_narx', 'max_sena',
                  )

        labels = {
            'nakladnoy': 'Номер накладная',
            'tovar': 'Названия препората',
            'olingan_soni': 'Количество прибытий',
            'ishlab_chiqaruvchi': 'Проиводитель',
            'dori_sertifikati': 'Сертификат препората',
            'olingan_narxi' : 'Закупная цена',
            'ustiga_foiz': 'Ставить проценты',
            'sotiladigan_narx': 'Цена продажы',
            'max_sena': 'Максимальная цена',
        }

