from django import forms
from django.forms import ModelForm

from users.models import User
from users.forms import UserRegisterForm, UserProfileForm
from products.models import ProductCategory

class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4','readonly': False}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control py-4', 'readonly': False}))


class ProductCategoryAdminCreateForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4'
        }))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control py-4'
        }))

    class Meta:
        model = ProductCategory
        fields = ['name', 'description']