from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            messages.success(request, "Account created successfully")
            return redirect('logIn')
    else:
        form = forms.RegisterForm()
    return render(request, './register.html', {'form': form, 'type': 'Register'})


def edit_profile(request):
    if request.method == 'POST':
        form = forms.ChangeUserFrom(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Changed successfully')
            return redirect('profile')
    form = forms.ChangeUserFrom(instance=request.user)
    return render(request, 'register.html', {'form': form, 'type': 'Edit profile'})


def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'password Changed successfully')
            return redirect('profile')
    form = PasswordChangeForm(user=request.user)
    return render(request, 'register.html', {'form': form, 'type': 'Change password'})

def set_pass(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'password Changed successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    form = SetPasswordForm(user=request.user)
    return render(request, 'register.html', {'form': form, 'type': 'Change password'})


def profile(request):
    return render(request, 'profile.html')


def logIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = name, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully")
                return redirect('profile')

    form = AuthenticationForm()
    return render(request, 'register.html', {'form':form, 'type': 'log in'})


def logOut(request):
    messages.success(request, "logged out successfully")
    logout(request)
    return redirect('homepage')