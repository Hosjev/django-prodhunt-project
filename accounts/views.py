from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            # passwds match
            try:
                user = User.objects.get(username=request.POST["username"])
                # reject if object TRUE
                return render(request, 'accounts/signup.html',
                              {'error': 'Username "' + request.POST["username"] + '" is already taken'})
            except User.DoesNotExist:
                # catch the exception here to add
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html',
                          {'error': 'Passwords do not match'})
    else:
        return render(request, 'accounts/signup.html')


def login(request):
    # if POST
    if request.method == "POST":
        user = auth.authenticate(
            username=request.POST["username"], password=request.POST["password1"])
        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',
                          {'error': 'Username or password is invalid'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
