from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from dorilar.models import Nakladnoy
import json


def main(request):
    return render(request, 'kassa/Main.html')


def table(request):
    return render(request, 'kassa/table.html')


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
            'tovar': response_obj.tovar.name,
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
        print(request.POST.get('chek'))
        data = json.loads(request.POST.get('chek'))
        print(data)
        return HttpResponse("Malades ukam")