from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Tovar, Nakladnoy, NakladnoyNo, Firma
from .forms import TovarForm, NakladnoyForm, NakladnoyNoForm, FirmaForm, TipTovara
from django.utils.timezone import now
from django.core import serializers


def glavni(request):
    hello = Nakladnoy.objects.all()
    return render(request, 'base.html', {"hello": hello})


def nakladnoy(request, id=0):
    #bu zapros metodini tekshiradi
    if request.method == "POST":
        #agar zapros post bolsa toldirilgan formani oladi va yangi nakladnoy hosil qiladi
        form = NakladnoyNoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/prixod/')
    else:
        #agar zapros metodi get bolsa
        if id == 0:
            form = TovarForm()
            nakladnoyi = NakladnoyNo.objects.all()
            nakladnotNoForm = NakladnoyNoForm()
            return render(
                request,
                'prixod/prixod.html',
                {
                    'form': form,
                    'nakladnoyi': nakladnoyi,
                    'nakladnotNoForm': nakladnotNoForm
                }
            )
        else:
            nakladnoy = Nakladnoy.objects.filter(nakladnoy__nakladnoy_nom=id)
            postavshik = NakladnoyNo.objects.get(nakladnoy_nom=id)
            tovarlar = Tovar.objects.all()
            tipTovara = TipTovara.objects.all()
            return render(
                request,
                'prixod/prixod_detail.html',
                {
                    'nakladnoyi': nakladnoy,
                    'nomer_nak': id,
                    'postavshik_nak': postavshik,
                    'tovarlar': tovarlar,
                    'tipTovara': tipTovara,
                }
            )


def create_dori(request):
    if request.method == "POST":
        shtrixKod = request.POST.get('shtrixKod')
        tip_tovara_id = request.POST.get('tip')
        tip_tovara = TipTovara.objects.get(id=tip_tovara_id)
        name = request.POST.get('name')
        shtukPachke = request.POST.get('shtukPachke')
        Tovar.objects.create(
            shtrixKod=shtrixKod,
            tip_tovara=tip_tovara,
            name=name,
            shtukPachke=shtukPachke,
        )
        return redirect('/prixod/')


def postavshik(request):
    if request.method == "GET":
        postavshiki = Firma.objects.all()
        firmaform = FirmaForm()
        return render(
            request,
            'prixod/postavshik.html',
            {
                'postavshiki': postavshiki,
                'firmaform': firmaform
            }
        )
    else:
        form = FirmaForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/prixod/')


def add_dori(request, id):
    if request.method == "POST":
        nakladnoy = NakladnoyNo.objects.get(nakladnoy_nom=id)
        tovar_id = request.POST.get('tovar')
        tovar = Tovar.objects.get(id=tovar_id)
        olingan_soni = request.POST.get('olingan_soni')
        ishlab_chiqaruvchi = request.POST.get('ishlab_chiqaruvchi')
        dori_sertifikati = request.POST.get('dori_sertifikati')
        srok = request.POST.get('srok')
        olingan_narxi = request.POST.get('olingan_narxi')
        ustiga_foiz = request.POST.get('ustiga_foiz')
        sotiladigan_narx = request.POST.get('sotiladigan_narx')
        max_sena = request.POST.get('max_sena')
        Nakladnoy.objects.create(
            nakladnoy=nakladnoy,
            tovar=tovar,
            olingan_soni=olingan_soni,
            ishlab_chiqaruvchi=ishlab_chiqaruvchi,
            dori_sertifikati=dori_sertifikati,
            srok=srok,
            olingan_narxi=olingan_narxi,
            ustiga_foiz=ustiga_foiz,
            sotiladigan_narx=sotiladigan_narx,
            max_sena=max_sena
        )
    return redirect('/prixod/{}'.format(id))


def deleteNakladnoy(request, id):
    willDelete = NakladnoyNo.objects.get(id=id)
    willDelete.delete()
    return redirect('/prixod/')


def deletePrixod(request, idd):
    willDelete = Nakladnoy.objects.get(id=idd)
    willDelete.delete()
    return redirect("/prixod/")


def pereotsenka(request):
    if request.method == "GET":
        dorilar = Nakladnoy.objects.all()
        list_dorilar = list(dorilar.values())
        list_names = []
        for dori in list_dorilar:
            list_names.append({
                "id": dori['id'],
                "name": str(Tovar.objects.get(id=dori['tovar_id'])),
                "nakladnoy": str(NakladnoyNo.objects.get(id=dori['nakladnoy_id'])),
                "date": str(dori['date_dobavlen'])
            })
        print(list_names)
    return render(
        request,
        'pereotsenka/pereotsenka.html',
        {
            "dorilar": dorilar,
            "list_dorilar": list_names
        }
    )


def newPereotsenka(request, id):
    return HttpResponse(id)


def spisaniya(request):
    return render(request, 'spisaniya/spisaniya.html')


def otchoti(request):
    return render(request, 'otchoti/otchoti.html')