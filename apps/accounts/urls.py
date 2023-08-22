from django.urls import path
from .views import (login_request, logout, mainpage, admin_dashboard, initial_calculation)

app_name = "accounts"

urlpatterns = [
    # path("", login_request, name="login"),
    path("login/", login_request, name="login"),
    path("logout/", logout, name="logout"),
    path("", mainpage, name="main_page"),
    path("dashboard/", admin_dashboard, name="admin_dashboard"),
    path("initail - calculation/", initial_calculation, name="initial_calculation"),

]
