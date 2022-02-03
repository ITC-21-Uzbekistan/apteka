from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Tovar, Nakladnoy, NakladnoyNo, Firma
from .forms import TovarForm, NakladnoyForm, NakladnoyNoForm, FirmaForm
import datetime
import django_filters
# def create_obj(request):
#     form = TovarForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     return render(request, 'hamma_dorilar/qoshish.html', {'form': form})


def glavni(request):
    return render(request, 'base.html')


def prixod(request, id=0):
    if request.method == "POST":
        if id == 0:
            form = NakladnoyNoForm(request.POST or None)
            if form.is_valid():
                form.save()
                return redirect('/prixod/')
        else:
            form = NakladnoyForm(request.POST or None)
            if form.is_valid():
                form.nakladnoy = NakladnoyNo.objects.get(nakladnoy_nom=id)['id']
                form.save()
                return redirect('/prixod/')
    else:
        if id == 0:
            vaqt = datetime.date.today()
            form = TovarForm()
            nakladnoyi = NakladnoyNo.objects.all()
            nakladnotNoForm = NakladnoyNoForm()
            return render(request, 'prixod/prixod.html',
                          {'form': form, 'vaqt': vaqt, 'nakladnoyi': nakladnoyi,
                           'nakladnotNoForm': nakladnotNoForm})
        else:
            nakladnoy = Nakladnoy.objects.filter(nakladnoy__nakladnoy_nom=id)
            postavshik = NakladnoyNo.objects.get(nakladnoy_nom=id)
            nakladchikform = NakladnoyForm()
            return render(request, 'prixod/prixod_detail.html',
                          {'nakladnoyi': nakladnoy, 'nomer_nak': id, 'postavshik_nak': postavshik, 'nakladchikform': nakladchikform})


def postavshik(request):
    if request.method == "GET":
        postavshiki = Firma.objects.all()
        firmaform = FirmaForm()
        return render(request, 'prixod/postavshik.html', {'postavshiki': postavshiki, 'firmaform': firmaform})
    else:
        form = FirmaForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/prixod/')


def prixod_detail(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = NakladnoyForm()
        else:
            nakladnoy = Nakladnoy.objects.get(id=id)
            form = NakladnoyForm(instance=nakladnoy)
        return render(request, 'prixod/prixod_detail.html', {'forma': form})
    else:
        if id == 0:
            form = NakladnoyForm(request.POST)
        else:
            nakladnoy = Nakladnoy.objects.get(id=id)
            form = NakladnoyForm(request.POST, instance=nakladnoy)
        if form.is_valid():
            form.save()
        return redirect('/prixod/')


def deleteNakladnoy(request, id):
    willDelete = NakladnoyNo.objects.get(id=id)
    willDelete.delete()
    return redirect('/prixod/')


def deletePrixod(request, idd):
    willDelete = Nakladnoy.objects.get(id=idd)
    willDelete.delete()
    return HttpResponse("Накладной удалена")


def pereotsenka(request):
    return render(request, 'pereotsenka/pereotsenka.html')


def spisaniya(request):
    return render(request, 'spisaniya/spisaniya.html')


def otchoti(request):
    return render(request, 'otchoti/otchoti.html')