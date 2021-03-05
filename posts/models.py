from django.db import models

from django.contrib.auth.models import User

# Documentacion de tablas relacionales en django
# https://docs.djangoproject.com/en/3.1/ref/models/fields/#module-django.db.models.fields.related


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # otra manera de llamar un modelo de otra app es poniendo el nombre
    # de la app seguido del nombre del modelo
    profile = models.ForeignKey("users.Profile", on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="posts/photos")

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """returns title and username"""
        return "{} by @ {}".format(self.title, self.user.username)
