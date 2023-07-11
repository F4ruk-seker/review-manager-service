from django import forms


class LoginForm(forms.Form):
    username = forms.Textarea()
    password = forms.Textarea()
