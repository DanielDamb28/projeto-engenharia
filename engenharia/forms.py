from django import forms


class LoginForm(forms.Form):
    login = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={"class":"login-field"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={"class":"password-login-field"}))

class RegisterForm(forms.Form):
    first_name = forms.CharField(label="", max_length=40, widget=forms.TextInput(attrs={"class":"first-field"}))
    last_name = forms.CharField(label="", max_length=40, widget=forms.TextInput(attrs={"class":"last-field"}))
    cpf = forms.CharField(label="", max_length=15, widget=forms.TextInput(attrs={"class": "cpf-field"}))
    email = forms.EmailField(label="", max_length=40, widget=forms.EmailInput(attrs={"class": "email-field"}))
    telefone = forms.CharField(label="", max_length=20, widget=forms.TextInput(attrs={"class": "telefone-field"}))
    password = forms.CharField(label="", max_length=30, widget=forms.PasswordInput(attrs={"class": "password-field"}))
    confirm_password = forms.CharField(label="", max_length=30, widget=forms.PasswordInput(attrs={"class": "confirm-password-field"}))