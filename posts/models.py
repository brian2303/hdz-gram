from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/3.1/ref/models/fields/


class User(models.Model):
    """User model"""

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    bio = models.TextField(blank=True)
    is_admin = models.BooleanField(default=False)
    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)