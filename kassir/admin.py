from django.contrib import admin
from .models import Kassir


class KassirAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'passport_seria', 'username', 'password']


admin.site.register(Kassir, KassirAdmin)
