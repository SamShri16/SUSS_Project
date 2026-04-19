from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if len(password) < 6:
            messages.error(request, "Password must be at least 6 characters")
            return redirect('/register/')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('/register/')

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Registered successfully")
        return redirect('/login/')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/dashboard/')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('/login/')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/login/')