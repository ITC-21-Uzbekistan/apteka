from django.urls import path

from kassir.views import kassirs, add_kassir, check_admin, log_out

urlpatterns = [
    path('', kassirs, name="kassirs"),
    path('addkassir/', add_kassir, name="addKassir"),
    path('login/', check_admin, name="checkadmin"),
    path('logout/', log_out, name="logOut"),
]