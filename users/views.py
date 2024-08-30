from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, LoginForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login_2.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return HttpResponse(f'Hello, {request.user.username}!')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            User = form.save()
            login(request, User)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})