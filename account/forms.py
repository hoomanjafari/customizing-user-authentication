from django import forms
from .models import Account


class AccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = Account
        fields = ('email', 'phone_number', 'username')


class LoginForm(forms.Form):
    phone_number = forms.IntegerField()
    password = forms.IntegerField()
