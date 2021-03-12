from django.urls import path

from . import views

urlpatterns = [
    path(
        route="",
        view=views.list_posts,
        name="feed"
    ),
    path(
        route="post/new",
        view=views.create_post,
        name="create_post"
    ),
]
