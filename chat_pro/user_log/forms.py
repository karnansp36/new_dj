from django import forms
from .models import UserSignup

class UserSignupForm(forms.ModelForm):
    class Meta:
        model = UserSignup
        exclude = ['created_at']
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput(),
            'username': forms.TextInput(attrs={'class': 'form-control container', 'placeholder': 'Enter Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'profile': forms.FileInput(attrs={'class': 'form-control'}),
        }
