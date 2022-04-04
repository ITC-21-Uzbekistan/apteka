from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from dorilar.models import Nakladnoy
import json
from kassir.models import Kassir
from logics.password_hash import check_password
from .models import Arxiv


def main(request):
    if request.method == "POST":
        username = str(request.POST.get('username'))
        if check_username(username):
            password = str(request.POST.get('password'))
            if check_kassir(username, password):
                return render(request, 'kassa/Main.html', {
                    "id": Kassir.objects.get(username=username).id,
                    "user": str(Kassir.objects.get(username=username).name)
                })
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return render(request, 'kassa/home.html')


def check_username(username):
    try:
        Kassir.objects.get(username=username)
        return True
    except:
        return False


def check_kassir(user, password):
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
