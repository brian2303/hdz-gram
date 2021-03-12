from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post
# Forms
from users.forms import ProfileForm, SignupForm


class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'users/detail.html'
    # Esto es como le llamamos al path converter en la url 'username'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    # Aca no trae todo los perfiles solamente el que estamos pidiendo por la url
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["posts"] = Post.objects.filter(user=user).order_by('-created')
        return context


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
            if data["picture"]:
                profile.picture = data["picture"]
            else:
                profile.picture = profile.picture
            profile.save()
            url = reverse('users:detail', kwargs={
                          'username': request.user.username})
            return redirect(url)
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
            return redirect("posts:feed")
        else:
            return render(request, "users/login.html", {"error": "Invalid credentials"})
    return render(request, "users/login.html")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")
    else:
        form = SignupForm()

    return render(
        request=request, template_name="users/signup.html", context={"form": form}
    )


@login_required
def logout_view(request):
    logout(request)
    return redirect("users:login")
