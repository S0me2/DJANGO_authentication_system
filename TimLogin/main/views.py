from django.shortcuts import redirect, render
from . forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from . forms import QuoteForm
from .models import Quote


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

# it is a decorator, smth in () tells where to redirect if user is not logged in
@login_required(login_url="/login/")
def home(request):
    quotes = Quote.objects.all()
    if request.method == "POST":
        quote_id = request.POST.get("quote-id")
        quote = Quote.objects.filter(id=quote_id).first()
        if quote and quote.creator == request.user:
            quote.delete()

    return render(request, 'main/home.html', {"quotes":quotes})

def logout_view(request):
    logout(request)
    return redirect('/login/')

def test_template(request):
    return render(request, 'registration/password_reset_do.html')

@login_required(login_url="/login/")
def create_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            # commit=False does not save the form in database as soon as it is saved
            quote = form.save(commit=False)
            quote.creator = request.user
            quote.save()
            return redirect("/home/")
    else:
        form = QuoteForm()
    return render(request, 'main/create_quote.html', {"form":form})



@login_required(login_url="/login/")
def my_quotes(request):
    quotes = Quote.objects.filter(creator=request.user)

    if request.method == "POST":
        quote_id = request.POST.get("quote-id")
        quote = Quote.objects.filter(id=quote_id).first()
        if quote and quote.creator == request.user:
            quote.delete()

    return render(request, "main/my_quotes.html", {"quotes": quotes})
