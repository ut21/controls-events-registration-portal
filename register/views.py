from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, ClubForm

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('add_event')
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again..."))	
            return redirect('login')	


    else:
        return render(request, 'register/login2.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, ("You Have Been Logged Out..."))
    return redirect('login')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('add_club')
    else:
        form = RegisterUserForm()

    return render(request, 'register/register.html', {
        'form':form,
        })

def add_club(request):
    if request.method == "POST":
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_event')
# return redirect('add_event')
            # return render (request, 'events_portal/', {
            #     "form": ClubForm(),
            # })

    
    return render (request, 'events_portal/add_event_club.html', {
        "form": ClubForm(),
    })