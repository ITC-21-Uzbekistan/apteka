from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from dorilar.models import Nakladnoy
import json
from kassir.models import Kassir
from logics.password_hash import check_password


def main(request):
    if request.method == "POST":
        username = str(request.POST.get('username'))
        if check_username(username):
            password = str(request.POST.get('password'))
            if check_kassir(username, password):
                return render(request, 'kassa/Main.html')
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
            'srok': '',
            'narx': '',
        },
        'except': '',
    }
    response_obj = None
    try:
        list_obj = Nakladnoy.objects.filter(tovar__shtrixKod=shtrixKod)
        if len(list_obj) == 1:
            response_obj = Nakladnoy.objects.get(tovar__shtrixKod=shtrixKod)
        else:
            when = []
            for i in list_obj:
                when.append(i.nakladnoy.id)

            naklad_id = int(min(when))
            for elem in list_obj:
                if elem.nakladnoy.id == naklad_id:
                    response_obj = elem
                    break
                else:
                    continue

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
        print(data)
        # if len(data) == 1:
        #     data = data[0]
        #     Shot.objects.create(
        #         tovar_id=data['id'],
        #         nakladnoy=data['nakladnoy'],
        #         tovar=data['tovar'],
        #         srok=data['srok'],
        #         narx=data['narx'],
        #         soni=data['soni'],
        #         summa=data['soni']
        #     )
        return HttpResponse("Malades ukam")
