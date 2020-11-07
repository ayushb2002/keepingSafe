from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("loadHospitals", views.loadHospitals, name="loadHospitals"),
    path("loadData", views.loadData, name="loadData"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("signUpUser", views.signUpUser, name="signUpUser"),
    path("logout", views.logout_view, name="logout"),
    path("signIn", views.signIn, name="signIn"),
    path("login_hosp", views.login_hosp, name="login_hosp"),
    path("logout_hosp", views.logout_hosp, name="logout_hosp"),
    path("signUpHospital", views.signUpHospital, name="signUpHospital"),
    path("addSlot", views.addSlot, name="addSlot"),
    path("slotDel", views.slotDel, name="slotDel"),
    path("addDoc", views.addDoc, name="addDoc"),
    path("delDoc", views.delDoc, name="delDoc"),
    path("loadHosp", views.loadHosp, name="loadHosp"),
    path("loadDoc", views.loadDoc, name="loadDoc"),
    path("bookSlot", views.bookSlot, name="bookSlot"),
    path("compApp", views.compApp, name="compApp"),
    path("signUpVol", views.signUpVol, name="signUpVol"),
    path("login_vol", views.login_vol, name="login_vol"),
    path("logout_vol", views.logout_vol, name="logout_vol")
]