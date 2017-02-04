from django import forms
from django.db import IntegrityError
from .models import Signup

class SignupForm(forms.ModelForm):
    class Meta:
        model=Signup
        fields=['email' , 'full_name']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        # email_base , provider = email.split("@")
        # domain , extension =provider.split('.')
        if  not 'edu' in email:
            raise forms.ValidationError("please put the extension as edu")
        return email

class ContactForm(forms.Form):
    email=forms.EmailField()
    full_name=forms.CharField()
    message=forms.CharField()
