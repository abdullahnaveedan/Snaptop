from django.shortcuts import render, redirect
from django.http import HttpResponse 

from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from .models import *
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import Http404

# Create your views here.

def index(request):
    param = {}
    if request.user.is_authenticated:
        username = request.user.username
        user = User.objects.get(username=username)
        profile_obj = profile.objects.get(username=request.user)
        param = {
            'image': profile_obj.profilepic
        }
    else:
        print("NO login detect")
    return render(request , "index.html", param)

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

def uploadreel(request):
    if request.user.is_authenticated:
        param = {}
        username = request.user.username
        user = User.objects.get(username=username)
        profile_obj = profile.objects.get(username=user)
        param = {
            'image': profile_obj.profilepic
        }

        if request.method == "POST":
            title = request.POST.get("title")
            discription = request.POST.get("discription")
            username = request.user
            video_file = request.FILES.get('videofile', None)
            video = ''
            if video_file:
                file_name = default_storage.save('profilepic/' + video_file.name, ContentFile(video_file.read()))
                video = file_name
            else:
                video = ''
            reelsupload(username = username, title = title, discription = discription, reels = video_file).save()
        return render(request,"uploadreels.html",param)

    return render(request,"signin.html")
    
def myprofile(request):
    param = {}
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        profile_obj = profile.objects.get(username=user)
        posts = reelsupload.objects.filter(username=request.user)
        
        param = {
            'image': profile_obj.profilepic,
            'user' : user,
            'profile_obj' : profile_obj,
            'counter' : posts.count(),
            'posts' : posts
        }
    return render(request, "manageprofile.html",param)

def editprofile(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        profile_obj = profile.objects.get(username=user)
        param = {
            'image': profile_obj.profilepic,
            'user' : user,
            'profile_obj' : profile_obj
        }

        if request.method == "POST":
            user = User.objects.get(username = request.user)

            # Update the user fields
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
           
            # user.save()

            location = request.POST.get("location")
            bio = request.POST.get("bio")
            image_file = request.FILES.get('displaypic', None)
            image = ''
            if image_file:
                file_name = default_storage.save('profilepic/' + image_file.name, ContentFile(image_file.read()))
                image = file_name
                userprofile = profile(username = user, bio = bio, profilepic = image, location = location)
                # userprofile.save()
            else:
                userprofile = profile(username = user, bio = bio, location = location)
                # userprofile.save()  
            return redirect("myprofile")
            
    return render(request, "editprofile.html", param)