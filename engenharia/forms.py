from django import forms


class LoginForm(forms.Form):
    login = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={"class":"login-field"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={"class":"password-field"}))
