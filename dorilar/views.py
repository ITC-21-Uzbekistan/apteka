from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Tovar, Nakladnoy, NakladnoyNo, Firma, Pereotsenka, Spisaniya
from .forms import TovarForm, NakladnoyForm, NakladnoyNoForm, FirmaForm, TipTovara
from django.utils.timezone import now


def glavni(request):
    if request.method == "POST":
        login = request.POST.get('login')
        password = request.POST.get('password')
        if login == 'admin' and password == '4451122':
            return redirect('/prixod/')
        else:
            return HttpResponse("Login or password is incorrect")
    else:
        return render(request, 'home.html')


def nakladnoy(request, id=0):
    #bu zapros metodini tekshiradi
    if request.method == "POST":
        #agar zapros post bolsa toldirilgan formani oladi va yangi nakladnoy hosil qiladi
        form = NakladnoyNoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/prixod/')
        else:
            return HttpResponse("Yemadi")
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
        name = request.POST.get('name').lower()
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
        obj = []
        pereotsen = Pereotsenka.objects.all()
        for elem in pereotsen:
            obj.append({
                'name': str(Nakladnoy.objects.get(id=elem.tovar_id).tovar.name),
                'naklad': int(Nakladnoy.objects.get(id=elem.tovar_id).nakladnoy.nakladnoy_nom),
                'changes': elem
            })

        return render(
            request,
            'pereotsenka/pereotsenka.html',
            {
                "pereotsenki": obj
            }
        )


def newPereotsenka(request, id):
    if request.method == "POST":
        will_get = Nakladnoy.objects.get(id=id)
        will_save = {
            "tovar_id": int(id),
            "eski_protsent": float(will_get.ustiga_foiz),
            "eski_narx": float(will_get.sotiladigan_narx),
            "yengi_foiz": float(request.POST.get('protsent')),
            "yengi_narx": float(request.POST.get('narx')),
        }
        Pereotsenka.objects.create(
            tovar_id=will_save['tovar_id'],
            eski_protsent=will_save['eski_protsent'],
            eski_narx=will_save['eski_narx'],
            yengi_foiz=will_save['yengi_foiz'],
            yengi_narx=will_save['yengi_narx']
        )
        will_get.ustiga_foiz=request.POST.get('protsent')
        will_get.sotiladigan_narx=request.POST.get('narx')
        will_get.save()
        return redirect('/pereotsenka/')
    else:
        will_change = Nakladnoy.objects.get(id=id)
        return render(request, 'pereotsenka/pereotsenirovat.html', {"data": will_change})


def get_tovar_by_shtrix(request):
    response = {
        'success': False,
        'message': "This tovar doesn't have",
        'data': []
    }
    try:
        will_get = request.GET['shtrix']
        lists = list(Nakladnoy.objects.filter(tovar__shtrixKod=will_get))
        response['success'] = True
        for obj in lists:
            response['data'].append({
                "id": int(obj.id),
                "name": str(obj.tovar.name),
                "nakladnoy": int(obj.nakladnoy.nakladnoy_nom),
                "srok": str(obj.srok),
                "date": str(obj.date_dobavlen)
            })
    except:
        response['success'] = False
        print("Bad")
    finally:
        return JsonResponse(response, safe=False)


def search_tovars(request):
    will_search = str(request.GET['data'])
    lists = list(Nakladnoy.objects.filter(tovar__name__contains=will_search))
    response = []
    for obj in lists:
        response.append({
            "id": int(obj.id),
            "name": str(obj.tovar.name),
            "nakladnoy": int(obj.nakladnoy.nakladnoy_nom),
            "srok": str(obj.srok),
            "date": str(obj.date_dobavlen)
        })
    return JsonResponse(response, safe=False)


def spisaniya(request):
    spisaniya = list(Spisaniya.objects.filter(spisano=False))
    obj = []
    for elem in spisaniya:
        obj.append({
            "tovar": str(Tovar.objects.get(id=elem.tovar)),
            "data": elem
        })

    return render(request, 'spisaniya/spisaniya.html', {'spisaniya': obj})


def new_spisaniya(request, id):
    obj = Nakladnoy.objects.get(id=id)
    pereotsenka = Pereotsenka.objects.get(tovar_id=id)
    Spisaniya.objects.create(
        nakladnoy=int(obj.nakladnoy.nakladnoy_nom),
        tovar=str(obj.tovar.id),
        olingan_soni=int(obj.olingan_soni),
        ishlab_chiqaruvchi=str(obj.ishlab_chiqaruvchi),
        dori_sertifikati=str(obj.dori_sertifikati),
        srok=obj.srok,
        date_dobavlen=obj.date_dobavlen,
        olingan_narxi=float(obj.olingan_narxi),
        ustiga_foiz=float(obj.ustiga_foiz),
        sotiladigan_narx=float(obj.sotiladigan_narx),
        spisano=False
    )
    pereotsenka.delete()
    obj.delete()
    return redirect('/spisaniya/')


def will_spisat(request):
    pass


def otchoti(request):
    return render(request, 'otchoti/otchoti.html')