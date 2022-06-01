from dataclasses import field
from django import forms
from .models import CustomUser

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = CustomUser
        fields = ["username", "password"]

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "password"]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        data = self.cleaned_data['password']
        if len(data) < 4:
            raise forms.ValidationError("Password should be more than 3 symbols.")
        
        return data
