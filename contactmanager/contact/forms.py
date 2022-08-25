from .models import *
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth import get_user_model


User = get_user_model()

class SignupForm(forms.Form):
    username = forms.CharField(
        label='User Name'
    )
    first_name = forms.CharField(
        label='First Name'
    )
    last_name = forms.CharField(
        label='Last Name'
    )
    email = forms.EmailField(
        label='Email Address'
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput
    )
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs  = User.objects.filter(username__iexact = username)
        if qs.exists():
            raise forms.ValidationError('This is an invalid Username , please pick another')
        if qs.count() > 1:
            raise forms.ValidationError('This is an invalid Username , please pick another')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact = email)
        if qs.exists():
            raise forms.ValidationError('This email is already in use')
        return email
    
    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2 :
            raise forms.ValidationError("Your passwords dont match")
        return password1
    

class SigninForm(forms.Form):

    username = forms.CharField(
        label='User Name'
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )

    # def username(self):
    #     username = self.cleaned_data.get('username')
    #     qs = User.objects.filter(username__iexact = username )
    #     if not qs.exists():
    #         raise forms.ValidationError('This is an Invalid Email Address ')
    #     return username
    
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class AddContactForm(forms.Form):
    first_name = forms.CharField(
        label='First Name'
    )
    last_name = forms.CharField(
        label='Last Name'
    )
    email = forms.EmailField(
        label='Email Address'
    )
    mobile = PhoneNumberField(
        required = True,
        widget = PhoneNumberPrefixWidget(initial='NG'),
        label="Phone Number",
        
    )
    alternate_number = PhoneNumberField(
        widget = PhoneNumberPrefixWidget(initial='NG'),
        required = False,
        label="Another Phone Number",
        
    )
    
