from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Gallery

def index(request):
    if request.user.is_authenticated:
        feeds = Gallery.objects.filter(User=request.user).order_by('-id')
        return render(request, "index.html", {"feeds": feeds})
    return redirect("usersignin")

def usersignin(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials")
    
    return render(request, "signin.html")

def usersignup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        
        if not all([username, email, password, confirmpassword]):
            messages.error(request, 'All fields are required.')
        elif confirmpassword != password:
            messages.error(request, "Passwords do not match")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Account created successfully")
            return redirect("usersignin")
    
    return render(request, "createuser.html")

def addimage(request):
    if request.method == 'POST':
        feedimage = request.FILES.get('feedimage')
        if feedimage:
            Gallery.objects.create(feedimage=feedimage, User=request.user)
            return redirect("index")
    return render(request, "newpost.html")

def view_image(request,pk):
    feeds = Gallery.objects.filter(pk=pk)
    return render(request,"image.html",{"feeds":feeds})
    
    


def newpost(request):
    if request.method == 'POST':
        feedimage = request.FILES.get('feedimage')
        description = request.POST.get("description")
        if feedimage:
            Gallery.objects.create(feedimage=feedimage, User=request.user)
            return redirect("index")
    return render(request, "newpost.html")

def logoutuser(request):
    logout(request)
    return redirect('usersignin')  # Redirect to sign-in page after logout

def delete_image(request,pk):
    feeds = Gallery.objects.filter(pk=pk)
    feeds.delete()
    return redirect("index")
    