from django.urls import path

from . import views

urlpatterns = [
    path(
        route="",
        view=views.PostsFeedView.as_view(),
        name="feed"
    ),
    path(
        route="post/new",
        view=views.create_post,
        name="create_post"
    ),
    path(
        route='post/<int:pk>',
        view=views.PostDetailView.as_view(),
        name='detail'
    )
]
