from django.shortcuts import redirect, render
from . forms import RegisterForm
from django.contrib.auth import login, logout, authenticate


def sign_up(request):
    # if it is a POST request, we will fill register form with input data(in the displayed form)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home/')
    # if it is a GET request, we will create a empty form and render it
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})

def home(request):
    return render(request, 'main/home.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')
