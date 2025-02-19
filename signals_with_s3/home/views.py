from django.shortcuts import render, redirect
from .models import Profile
from . models import User
from django.contrib import messages
from . forms import UserUpdateForm, ProfileUpdateForm, UserRegistrationForm

def home(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'home/index.html', context)

def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, "Account created successfully!")
            return redirect('home')
    context = {'form': form}
    return render(request, 'home/register.html', context)

def optionPage(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    context = {'profile': profile}
    return render(request, 'home/option.html', context)

def deleteFunc(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    profile.delete()
    messages.success(request, "Account deleted successfully!")
    return redirect('home')

def updateFunc(request, username):
    user = User.objects.get(username=username)
    profile = user.profile
    u_form = UserUpdateForm(instance=user)
    p_form = ProfileUpdateForm(instance=profile)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profile updated successfully!")
            return redirect('home')
    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'home/update.html', context)

