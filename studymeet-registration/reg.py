#Importing
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import Feature
from django.contrib import messages

#Function
def register(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Email = request.POST['email']
        Passwort = request.POST['passwort']
        Passwort2 = request.POST['passwort2']
        if passwort == passwort2:
            if User.object.filter(email==email).exists():
                return redirect('register')
            elif User.object.filter(username==username).exists():
                    messages.info(request, "Username existiert")
                    return redirect('register')
            else:
                        user = User.object.create_user(username=username, Email=Email, Passwort=Passwort)
                        user.save("test_1")
                        return redirect('Login')
        else:
                            messages.info(request, 'Passwort stimmt nicht überein')
                            return redirect('register')
    else:
                                return render(request, 'reg.html')

