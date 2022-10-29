from email.policy import default
from django.db import models

class Profile(models.Model):
    slackUsername = models.CharField(max_length=150)
    backend = models.BooleanField(default=True)
    age = models.IntegerField()
    bio = models.TextField()
