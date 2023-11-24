from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = [
    path("",views.index,name="index"),
    path("userprofile",views.userprofile, name="profile"),
    path("signin/",views.signin,name="signin"),
    path("signinform", views.signinform, name="signin"),
    path("signupform", views.signupform, name="signup"),
    path("logoutuser", views.logoutuser, name="logoutuser"),
    path("saveprofile", views.saveprofile , name = "saveprofile")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
