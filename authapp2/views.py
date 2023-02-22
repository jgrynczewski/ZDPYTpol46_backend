from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='authapp2:login-view')
def home(request):
    return render(
        request,
        'authapp2/home.html'
    )


# Widok wszystkich użytkowników
# all users (najszybciej, po prostu w shellu)
def user_list_view(request):
    users = User.objects.all()

    return render(
        request,
        'authapp2/users.html',
        context={
            'users': users,
        }
    )


# Rejestracja (C w User)
def register_view(request):
    if request.method == "GET":
        return render(
            request,
            'authapp2/register.html',
        )

    elif request.method == "POST":
        data = request.POST

        username = data.get('username')
        password = data.get('password')
        password2 = data.get('password2')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')

        User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        return redirect('authapp2:login-view')


# Widok logowania
def login_view(request):
    if request.method == "GET":
        return render(
            request,
            'authapp2/login.html',
        )

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)  # uwierzytelnienie

        if user:
            login(request, user)

        return redirect('authapp2:home')


def logout_view(request):
    logout(request)
    return redirect('authapp2:home')


# permission_required
# formapp2/views/contact3
