# hier stehen die klassen und aus welchem module sie importiert werden
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse

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
    if request.method == "POST":
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
    return render(request, 'hostart/register.html', {'register_form': register_form})


def vlogin(request):
    login_form = AuthenticationForm()
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
    return render(request, 'hostart/login.html', {'login_form': login_form})


def vlogout(request):
    logout(request)
    return redirect(reverse('hostart:index'))
