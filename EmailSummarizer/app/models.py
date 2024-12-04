from django.contrib.auth.models import User
from django.db import models

#  Stores authentication-related information for the Gmail API.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #email = models.EmailField(unique=True)
    access_token = models.TextField(blank=True, null=True)
    refresh_token = models.TextField(blank=True, null=True)
    #token_expiry = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username

#  Stores the topics that the user has created.
class Topic(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="topics")
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.user.user.username})"

