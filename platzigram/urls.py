from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from platzigram import views as local_views
from posts import views as posts_views
from users import views as user_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello-world", local_views.hello_world, name="hello_world"),
    path("hi", local_views.hi, name="hi"),
    path("challenge-number", local_views.challenge_numbers, name="challenge"),
    path("say-hi/<str:name>/<int:age>/", local_views.say_hi, name="say-hi"),
    # posts views
    path("", posts_views.list_posts, name="feed"),
    path("post/new", posts_views.create_post, name="create_post"),
    # user views
    path("users/login/", user_views.login_view, name="login"),
    path("users/logout/", user_views.logout_view, name="logout"),
    path("users/signup", user_views.signup, name="signup"),
    path("users/me/profile", user_views.update_profile, name="update_profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
