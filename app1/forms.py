from django import forms
from .models import Register,Image
class RegisterForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=Register
        fields='__all__'

class ImageUploadForm(forms.ModelForm):
    class Meta():
        model=Image
        fields='__all__'

class LoginForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=Register
        fields=('Email','Password',)

class UpdateForm(forms.ModelForm):
    
    class Meta():
        model=Register
        fields=('Name','Age','Place','Email',)

class ChangePasswordForm(forms.Form):
    OldPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    NewPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)