from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import UserCreateForm

def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signupaccount.html', {'form': UserCreateForm()})
    else:
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            
            role = form.cleaned_data.get('role')
            profile = Profile(user=user, role=role)
            profile.save()

            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to home page after successful signup
        else:
            return render(request, 'signupaccount.html', {'form': form})


@login_required
def logoutaccount(request):
    logout(request)
    return redirect('logoutmessage')

def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            return render(request, 'loginaccount.html', {
                'form': AuthenticationForm(),
                'error': 'Username and password do not match.'
            })
        else:
            login(request, user)
            return redirect('home')
