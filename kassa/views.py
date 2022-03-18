from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    return render(request, 'kassa/Main.html')


def table(request):
    return render(request, 'kassa/table.html')