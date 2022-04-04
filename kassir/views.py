from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Kassir
from logics import password_hash


class Bekki:
    def __init__(self):
        self.checking_admin = False

    def setCheckingAmin(self):
        self.checking_admin = False

    def make_true(self):
        self.checking_admin = True


checking_admin_obj = Bekki()


def kassirs(request):
    if checking_admin_obj.checking_admin:
        return render(request, 'kassir/home.html', {'data': Kassir.objects.all()})
    else:
        return redirect('/admin/kassir/login/')


def check_admin(request):
    if request.method == "POST":
        if request.POST.get('username') == "admin":
            if request.POST.get('password') == "4451122":
                checking_admin_obj.make_true()
                return redirect('/admin/kassir/')
            else:
                return redirect('/admin/kassir/login/')
        else:
            return redirect('/admin/kassir/login/')
    else:
        return render(request, 'kassir/check.html')


def log_out(request):
    checking_admin_obj.setCheckingAmin()
    return redirect('/admin/kassir/')


def add_kassir(request):
    # print(checking_admin_obj.checking_admin)
    if request.method == "POST":
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        passport = request.POST.get('passport')
        username = request.POST.get('username')
        password = password_hash.hash_password(request.POST.get('password'))
        Kassir.objects.create(
            name=name,
            surname=surname,
            passport_seria=passport,
            username=username,
            password=password
        )
    return redirect('/admin/kassir/')
