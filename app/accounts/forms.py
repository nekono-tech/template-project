from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="ユーザー名",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "ユーザー名を入力してください",
            }
        ),
    )
    password = forms.CharField(
        label="パスワード",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "パスワードを入力してください",
            }
        ),
    )
