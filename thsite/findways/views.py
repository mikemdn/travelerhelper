# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from findways.backend.api_front import api
from .models import Profile


def process_instructions(array):
    """Store all the indications to display to the user"""
    elements_to_display = []
    return elements_to_display
"""
for way in array.items():
    way_infos = {}
    way_infos['mean_of_transport'] = way[0]
    way_infos['time'] = str(way[1][0])
    way_infos['distance'] = str(way[1][1])
    way_infos['cost'] = str(way[1][2])
    instructions = []
    for elemWay in way[1][-1]:
        for elem_step in elemWay[1][-1]:
            instructions.append(elem_step['instruction'])
    way_infos['instructions'] = instructions
    elements_to_display.append(way_infos)
"""


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
    show_result = False

    if request.method == "POST":
        form = TravelForm(request.POST)
        if form.is_valid():
            show_result = True
            data = form.cleaned_data
            json1 = {'destination': data['destination'], 'car': request.user.profile.car, 'driving licence': request.user.profile.licence,
                    'navigo': request.user.profile.navigo, 'credit card': request.user.profile.card, 'criteria': int(data['criteria'])}
            json2 = api.ApiRoute(json1).data_structure()
            results = process_instructions(json2)
    else:
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
    username = forms.CharField(label="Username ", max_length=30)
    password = forms.CharField(label="Password ", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label="Username ", max_length=30)
    mail = forms.CharField(label="E-mail ", max_length=50)
    password = forms.CharField(label="Password ", widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['licence', 'card', 'navigo', 'velibPass','car', 'bike']


class TravelForm(forms.Form):
    destination = forms.CharField(label = "Destination", max_length = 100)
    CHOICES = [(1, 'The faster'), (2, 'The cheaper'), (3, 'The most convenient if I carry heavy loads'), (4, 'Visit the city !')]

    criteria = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
