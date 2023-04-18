from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login_user')
        else:
            #messages.error(request, 'Username OR password is incorrect')
            return redirect('login_user')
    else:
        return render(request, 'authenticate/login.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Account was created for ' + username)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'authenticate/register_user.html', {
        'form': form,
    })
