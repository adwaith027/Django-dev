from django import forms
from django.core.validators import validate_email
from .models import userlog

class signform(forms.ModelForm):
    class Meta:
        model=userlog
        fields=['uname','email','password','confirm_password']

class logform(forms.ModelForm):
    class Meta:
        model=userlog
        fields=['email','password']