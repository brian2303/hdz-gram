from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Forms
from users.forms import ProfileForm, SignupForm


@login_required
def update_profile(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            data = form.cleaned_data
            profile.website = data["website"]
            profile.biography = data["biography"]
            profile.phone_number = data["phone_number"]
            import pdb

            pdb.set_trace()
            if data["picture"]:
                profile.picture = data["picture"]
            else:
                profile.picture = profile.picture
            profile.save()
            return redirect("update_profile")
    else:
        form = ProfileForm()
    return render(
        request=request,
        template_name="users/update_profile.html",
        context={"profile": profile, "user": request.user, "form": form},
    )


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user=user)
            return redirect("feed")
        else:
            return render(request, "users/login.html", {"error": "Invalid credentials"})
    return render(request, "users/login.html")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignupForm()

    return render(
        request=request, template_name="users/signup.html", context={"form": form}
    )


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")
