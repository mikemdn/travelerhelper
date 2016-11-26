from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse

from django.views import generic

# Create your views here.

# def index(request):
#     text = """<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Index</title>
# </head>
# <body>
# <h1>Bienvenue sur traveler helper</h1>
# <button>Se connecter</button>
# <button>S'inscrire</button>
#
# </body>
# </html>"""
#     return HttpResponse(text)

def index(request):
    return render(request,'findways/index.html')

def signup(request):
    error = False
    userAlreadyExists = False
    userIsCreated = False
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            userIsCreated = True
            user = User.objects.create_user(form.cleaned_data['username'], None, form.cleaned_data['password1'])
            user.save()
            return redirect('http://localhost:8000/findways/signin/')
    else:
        form = UserCreationForm()

    return render(request, 'findways/signup.html', locals())



def signin(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'findways/signin.html', locals())

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    mail = forms.CharField(label="E-mail address", max_length=50)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

def mytravel(request):
    return HttpResponse("coucou")