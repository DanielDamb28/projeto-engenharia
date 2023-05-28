from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm, RegisterForm
from .models import Usuario

# Create your views here.

def login_screen(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = Usuario()
            cpf = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = Usuario.objects.filter(cpf=cpf)
            if user[0]:
                return HttpResponse(f"Login: {user[0].first_name} <br>")
            else:
                return HttpResponse(f"Usuario Invalido")
    else:
        form = LoginForm()
        return render(request, 'engenharia/login-screen.html', {"form": form})
    
def register_screen(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        user = Usuario()
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.cpf = form.cleaned_data['cpf']
            user.password = form.cleaned_data['password']
            user.telefone = form.cleaned_data['telefone']
            user.save()
            return HttpResponse(f"Usuario Cadastrado com Sucesso first name = {user.first_name} last_name = {user.cpf}")
        else:
            return HttpResponse(f"{form.fields}")

    else:
        form = RegisterForm()
        return render(request, 'engenharia/register-screen.html', {"form": form})
