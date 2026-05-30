from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect("courses")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("courses")
        
        messages.error(request, "Неверный логин или пароль")

    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")
