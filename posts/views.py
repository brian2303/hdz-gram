from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from posts.forms import PostForm

from posts.models import Post


class PostsFeedView(LoginRequiredMixin, ListView):
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 10
    # Con este atributo indicamos que queremos que el model = Post que declaramos arriba en la vista se llame posts
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'posts/detail.html'
    # No trae todos los posts por que con este query DetailView sabe como traer solo el que necesitamos
    queryset = Post.objects.all()
    # Es el nombre con el que se utilizara en el template
    context_object_name = 'post'


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("posts:feed")
    else:
        form = PostForm()
    return render(
        request=request,
        template_name="posts/new.html",
        context={
            "form": form,
            "user": request.user,
            "profile": request.user.profile,
        },
    )
