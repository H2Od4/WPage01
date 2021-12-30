# hier stehen die klassen und aus welchem module sie importiert weren
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render

# hier wird eine funktion definiert und als  http://127.0.0.1:8000/
# ist eine Variable "request" definiert


def vindex(request):
    # die Rückgabeparameter wird die Funtkiton "render" zurückgegeben
    # welches die übergebene "request" inhalt mit der "url" enthaltene
    # HTML seite so einsetzt "render" dass die Seite als Hompage-Seite
    # dargestellt werden kann
    return render(request, 'hostart/base.html')


def vregister(request):
    register_form = UserCreationForm()
    return render(request, 'hostart/register.html', {'register_form': register_form})


def vlogin(request):
    login_form = AuthenticationForm()
    return render(request, 'hostart/login.html', {'login_form': login_form})
