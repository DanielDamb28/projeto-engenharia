from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm

# Create your views here.

def login_screen(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return HttpResponse(f"Login: {data['login']} <br> Password: {data['password']}")
    else:
        form = LoginForm()
        return render(request, 'engenharia/login-screen.html', {"form": form})
