from django.db import models


class UserProfile(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    technologies=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    display_picture=models.FileField()
    def __str__(self):
        return self.fname