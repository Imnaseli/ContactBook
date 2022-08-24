from django.contrib import admin
from .models import *
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget
# Register your models here.


admin.site.register(Contact)
