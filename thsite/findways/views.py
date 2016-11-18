from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

# Create your views here.

def index(request):
    text = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Index</title>
</head>
<body>
<h1>Bienvenue sur traveler helper</h1>
<button>Se connecter</button>
<button>S'inscrire</button>

</body>
</html>"""
    return HttpResponse(text)
