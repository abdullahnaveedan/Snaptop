from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = [
    path("",views.index,name="index"),
    path("userprofile",views.userprofile, name="profile"),
    path("signin/",views.signin,name="signin"),
    path("myprofile/",views.myprofile,name="myprofile"),
    path("uploadreel/",views.uploadreel,name="uploadreel"),
    path("signinform", views.signinform, name="signin"),
    path("signupform", views.signupform, name="signup"),
    path("logoutuser", views.logoutuser, name="logoutuser"),
    path("saveprofile", views.saveprofile , name = "saveprofile"),
    path("editprofile", views.editprofile, name = "editprofile"),
    path("chat", views.chat,  name="chat"), 
    path("chat/", views.chatbox, name="chatbox")

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
