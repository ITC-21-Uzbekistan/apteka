from django.urls import path

from kassir.views import kassirs

urlpatterns = [
    path('', kassirs, name="kassirs")
]
