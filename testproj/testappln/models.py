from django.db import models
from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class userlog(models.Model):
    uname=models.CharField(max_length=20)
    email=models.CharField(max_length=25,validators=[validate_email])
    password=models.CharField(max_length=12)
    confirm_password=models.CharField(max_length=12)

    def match(self):
        if self.password != self.confirm_password:
            raise ValidationError('Passwords donot match')