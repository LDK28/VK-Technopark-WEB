from dataclasses import field
from dis import dis
from django import forms
from .models import CustomUser, Question

# class UserForm(forms.ModelForm):
#     username = forms.CharField(widget=forms.Textarea)
#     class Meta:
#         model = CustomUser
#         fields = ["username", "password"]

class RegistrationForm(forms.ModelForm):
    repeat_password = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email", "password"]
    
    def clean_password(self):
        data = self.cleaned_data.get('password')
        if len(data) < 4:
            raise forms.ValidationError("Password should be more than 3 symbols.")
        # if data != self.cleaned_data.get('repeat_password'):
        #     print("ERROR")
        #     print(data)
        #     print( self.cleaned_data.get('repeat_password'))
        #     raise forms.ValidationError("Passwords don't match")
        
        
        return data

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        data = self.cleaned_data['password']
        if len(data) < 4:
            raise forms.ValidationError("Password should be more than 3 symbols.")
        
        return data

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["title", "text"]

class SettingsForm(forms.ModelForm):
    username = forms.CharField(disabled=True)

    class Meta:
        model = CustomUser
        fields = ["username", "last_name", "first_name", "avatar", "email"]

    
    def save(self, *args, **kwargs):
        user = super().save()
        
        user.avatar = self.cleaned_data['avatar']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()
        return user