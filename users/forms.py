from django import forms
from django.contrib.auth.models import User

from users.models import Profile


class SignupForm(forms.Form):
    username = forms.CharField(
        min_length=4,
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        max_length=70, widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password_confirmation = forms.CharField(
        max_length=70, widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    first_name = forms.CharField(
        min_length=2,
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )

    # Esta es una validacion que nosotros personalizamos para comprobar que el usuario no se encuentre en sistema
    def clean_username(self):
        # https://docs.djangoproject.com/en/3.1/ref/forms/validation/
        # en la documentacion que dejo arriba se especifica todos los pasos que sigue django para validar un form
        username = self.cleaned_data["username"]
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError("Username is already in use")
        return username

    def clean(self):
        data = super().clean()
        password = data["password"]
        password_confirmation = data["password_confirmation"]

        if password != password_confirmation:
            raise forms.ValidationError("Passwords don't match")

        return data

    def save(self):
        data = self.cleaned_data
        data.pop("password_confirmation")

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


class ProfileForm(forms.Form):
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=10, required=False)
    picture = forms.ImageField(required=False)