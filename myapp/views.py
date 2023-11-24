from django.shortcuts import render, redirect
from django.http import HttpResponse 

from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from .models import profile
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
# Create your views here.

def index(request):

    if request.user.is_authenticated:
        print("==>>>",request.user.username)
    else:
        print("NO login detect")
    return render(request , "index.html")

def signin(request):
    return render(request, "signin.html")

def signinform(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username = username,password = password)
        if user is not None:
            auth_login(request, user)
            return redirect("index")

    return render(request, "signin.html")

def userprofile(request):
    
    return render(request , "profile.html")

def signupform(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmPassword = request.POST.get("confirmPassword")
        if password == confirmPassword:
            user = User.objects.create_user(username = username , email = email, password = password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("profile")

    return render(request, "signin.html")

def logoutuser(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect("index")
    else:
        print("no account login")
    return redirect("index")
def saveprofile(request):
    if request.method == "POST":
        
        user = request.user
        location = request.POST.get("location")
        bio = request.POST.get("bio")
        image_file = request.FILES.get('displaypic', None)
        image = ''
        if image_file:
            file_name = default_storage.save('profilepic/' + image_file.name, ContentFile(image_file.read()))
            image = file_name
        else:
            image = ''

        userprofile = profile(username = user, bio = bio, profilepic = image, location = location)
        userprofile.save()
    return redirect("index")