from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout

from .models import Profile


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

@login_required(login_url='http://localhost:8000/findways/signin')
def mytravel(request):
    if request.method == "POST":
        form = TravelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            json = {'destination': data['destination'],'car': request.user.profile.car, 'driving licence': request.user.profile.licence,
                    'navigo': request.user.profile.navigo, 'credit card': request.user.profile.card, 'criteria' : int(data['criteria'])}

            print(json)
            return redirect("http://localhost:8000/findways/mytravel")
    else :
        form = TravelForm()

    return render(request, 'findways/mytravel.html', locals())

def log_out(request):
    logout(request)
    return redirect("http://localhost:8000/findways/")

def edit_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("http://localhost:8000/findways/mytravel")
    else :
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'findways/edit_profile.html', locals())


###################################################################################################################
# FORMS

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur ", max_length=30)
    password = forms.CharField(label="Mot de passe ", widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur ", max_length=30)
    mail = forms.CharField(label="E-mail address ", max_length=50)
    password = forms.CharField(label="Mot de passe ", widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['licence', 'card', 'navigo', 'velibPass','car', 'bike']

class TravelForm(forms.Form):
    destination = forms.CharField(label = "Destination", max_length = 100)
    CHOICES = [(1, 'Le plus rapide'),(2,'Le moins cher'),(3, 'Le plus pratique si je suis chargé'),(4, 'Celui qui me fait le plus visiter')]

    criteria = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())



