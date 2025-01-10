from django import forms
from .models import UserProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['fname','lname','technologies','email','display_picture']