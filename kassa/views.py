from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from dorilar.models import Nakladnoy
import json
from kassir.models import Kassir
from logics.password_hash import check_password
from .models import Arxiv
from django.views.generic.base import RedirectView


class Bekki:
    def __init__(self):
        self.checking_kassir = False
        self.username = None

    def make_false(self):
        self.checking_kassir = False

    def make_true(self):
        self.checking_kassir = True


checking_kassir = Bekki()


def main(request):
    if checking_kassir.checking_kassir:
        return render(request, 'kassa/Main.html', {
            'id': Kassir.objects.get(username=checking_kassir.username).id,
            'user': Kassir.objects.get(username=checking_kassir.username).name
        })
    else:
        return redirect('/login/')


# authontification in kassa

def authontification(request):
    if request.method == "POST":
        checking_kassir.username = request.POST.get('username')
        password = request.POST.get('password')
        if check_username(checking_kassir.username):
            if check_kassir_password(checking_kassir.username, password):
                checking_kassir.make_true()
                return redirect('/')
            else:
                return redirect('/login/')
        else:
            return redirect('/login/')
    else:
        return render(request, 'kassa/home.html')


# log out from kassa

def log_out_from_kassa(request):
    checking_kassir.make_false()
    return redirect('/')


def check_username(username):
    try:
        Kassir.objects.get(username=username)
        return True
    except:
        return False


# search tovars which was sold


def search_arxiv(request):
    will_search = str(request.GET['data'])
    lists = list(Arxiv.objects.filter(tovar_name__contains=will_search))
    response = []
    for obj in lists:
        response.append({
            "id": int(obj.id),
            "name": str(obj.tovar_name),
            "tovar_id": int(obj.tovar_id),
            "narx": float(obj.narx),
            "soni": int(obj.soni),
            "sold_time": obj.sold,
            "srok": str(obj.srok),
            "kassir": str(obj.user.name)
        })
    return JsonResponse(response, safe=False)


# search and get tovars from arxiv


def search_from_arxiv_by_shtrix(request):
    response = {
        'success': False,
        'message': "This tovar doesn't have",
        'data': []
    }
    try:
        will_get = request.GET['shtrix']
        lists = list(Arxiv.objects.filter(tovar_shtrix_kod=will_get))
        response['success'] = True
        for obj in lists:
            response['data'].append({
                "id": int(obj.id),
                "name": str(obj.tovar_name),
                "tovar_id": int(obj.tovar_id),
                "narx": float(obj.narx),
                "soni": int(obj.soni),
                "sold_time": obj.sold,
                "srok": str(obj.srok),
                "kassir": str(obj.user.name)
            })
    except:
        response['success'] = False
        print("Bad")
    finally:
        return JsonResponse(response, safe=False)


def do_vozvrat(request):
    print(request.POST.get('id'))
    id = request.POST.get('id')
    soni = request.POST.get('soni')

    will_vozvrat = Arxiv.objects.get(id=id)

    if will_vozvrat.soni == 1:
        tovar = Nakladnoy.objects.get(id=will_vozvrat.tovar_id)
        tovar.olingan_soni += 1
        tovar.save()
        will_vozvrat.delete()
    else:
        pass


def check_kassir_password(user, password):
    user = Kassir.objects.get(username=user)
    if check_password(user.password, password):
        return True
    else:
        return False


def get_shtrixkod(request):
    shtrixKod = str(request.GET['shtrixKod'])
    response = {
        'tovar': {
            'id': 0,
            'nakladnoy': 0,
            'tovar': '',
            'tovar_id': 0,
            'srok': '',
            'narx': '',
        },
        'except': '',
    }
    response_obj = None
    try:
        list_obj = Nakladnoy.objects.filter(tovar__shtrixKod=shtrixKod)
        when = []

        if len(list_obj) == 1:
            response_obj = Nakladnoy.objects.get(tovar__shtrixKod=shtrixKod)
        else:
            for i in list_obj:
                when.append(i.id)

            response_obj = Nakladnoy.objects.get(id=min(when))

        response['tovar'] = {
            'id': response_obj.id,
            'nakladnoy': response_obj.nakladnoy.nakladnoy_nom,
            'tovar': {
                'name': response_obj.tovar.name,
                'shtrixKod': response_obj.tovar.shtrixKod,
                'tip_tovara': response_obj.tovar.tip_tovara.tip,
                'shtukPachke': response_obj.tovar.shtukPachke
            },
            'srok': str(response_obj.srok),
            'narx': float(response_obj.sotiladigan_narx),
        }
    except Exception as ex:
        response['except'] = str(ex)
    finally:
        print("Response have sent")

    print(response)
    return JsonResponse(response, safe=False)


def make_pay(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('chek'))

        if len(data) == 1:
            data = data[0]
            Arxiv.objects.create(
                nakladnoy=data['nakladnoy'],
                tovar_id=data['id'],
                tovar_name=data['tovar']['name'],
                tovar_shtrix_kod=data['tovar']['shtrixKod'],
                tovar_shtuk_pachke=data['tovar']['shtukPachke'],
                tovar_type=data['tovar']['tip_tovara'],
                srok=data['srok'],
                narx=data['narx'],
                soni=data['soni'],
                summa=data['summa'],
                user=Kassir.objects.get(id=data['user'])
            )
            if Nakladnoy.objects.get(id=data['id']).olingan_soni - data['soni'] == 0:
                will_delete = Nakladnoy.objects.get(id=data['id'])
                will_delete.delete()
            else:
                will_minus = Nakladnoy.objects.get(id=data['id'])
                will_minus.olingan_soni -= int(data['soni'])
                will_minus.save()
        else:
            for tovar in data:
                Arxiv.objects.create(
                    nakladnoy=tovar['nakladnoy'],
                    tovar_id=tovar['id'],
                    tovar_name=tovar['tovar']['name'],
                    tovar_shtrix_kod=tovar['tovar']['shtrixKod'],
                    tovar_shtuk_pachke=tovar['tovar']['shtukPachke'],
                    tovar_type=tovar['tovar']['tip_tovara'],
                    srok=tovar['srok'],
                    narx=tovar['narx'],
                    soni=tovar['soni'],
                    summa=tovar['summa'],
                    user=Kassir.objects.get(id=tovar['user'])
                )
                if Nakladnoy.objects.get(id=tovar['id']).olingan_soni - tovar['soni'] == 0:
                    will_delete = Nakladnoy.objects.get(id=tovar['id'])
                    will_delete.delete()
                else:
                    will_minus = Nakladnoy.objects.get(id=tovar['id'])
                    will_minus.olingan_soni -= int(tovar['soni'])
                    will_minus.save()

        return HttpResponse("SUCCESS")
