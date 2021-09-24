from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=50)
    profile_url = models.TextField()
    google_id = models.TextField()