from django import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
import django_filter.rest_framework
from myapp.serializers import UserSerializer
from rest_framework import generics
from rest_framework import filters


#View Creation
def index(request):
    features = Feature.objects.all()
    return render(request, "index.html", {"features": features})

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        username = request.POST["email"]
        username = request.POST["passwort"]
        username = request.POST["passwort2"]

        if passwort == passwort2:
            if User.object.filter(email==email).exists():
                messages.info(request, "Email exisitiert")
                return redirect('reg')
            elif User.object.filter(username==username).exists():
                    messages.info(request, "Username existiert")
                    return redirect('reg')
            else:
                user = User.object.create_user(username=username, email=email, passwort=passwort)
                user.save("reg.sql")
                return redirect('Login')
        else:
            messages.info(request, 'Passwort stimmt nicht überein')
            return redirect('reg')
    else:
        return render(request, 'reg.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwort = request.POST['passwort']
        user = auth.authenticate(username = username, passwort = passwort)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Fehler')
            return redirect('login')
    else:
        return render(request, 'login.html', {})
