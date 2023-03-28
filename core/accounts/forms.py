from django import forms
from accounts.models import Choice
from django.contrib.auth import get_user_model
from .models import Account


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60, required=True, label='Логин')
    password = forms.CharField(max_length=70, required=True, label='Пароль', widget=forms.PasswordInput)


class CreateUser(forms.ModelForm):
    password = forms.CharField(label='Пароль', required=True, strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтвержение пароля', required=True, strip=False, widget=forms.PasswordInput)
    gender = forms.ChoiceField(label='Пол', required=False, choices=Choice.choices)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'avatar', 'password', 'password_confirm', 'first_name', 'last_name', 'info', 'phone', 'gender')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'avatar', 'gender', 'phone', 'info')
        labels = {
            'email': 'Почта',
            'avatar': 'Аватар',
            'gender': 'Пол',
            'phone': 'Телефон',
            'info': 'Информация'
        }


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(label="Новый пароль", strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, strip=False)
    old_password = forms.CharField(label="Старый пароль", strip=False, widget=forms.PasswordInput)

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        return password_confirm

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Старый пароль неправильный!')
        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['old_password', 'password', 'password_confirm']