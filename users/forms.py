from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите имя пользователя'
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите пароль'
        }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите имя пользователя'
        }))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите адрес эл. почты'
        }))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите имя'
        }))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите фамилию'
        }))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите пароль'
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Подтвердите пароль'
        }))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1',
                  'password2')


    def clean_username(self):
        data = self.cleaned_data['username']
        if len(data) < 2:
            raise forms.ValidationError(
                "Имя пользователя должно содержать больше 1 символа!")
        return data

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if len(data) < 2:
            raise forms.ValidationError(
                "Имя должно содержать больше 1 символа!")
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        if len(data) < 2:
            raise forms.ValidationError(
                "Фамилия должна содержать больше 1 символа!")
        return data


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4','readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control py-4', 'readonly': True}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image')


    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if len(data) < 2:
            raise forms.ValidationError(
                "Имя должно содержать больше 1 символа!")
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        if len(data) < 2:
            raise forms.ValidationError(
                "Фамилия должна содержать больше 1 символа!")
        return data
