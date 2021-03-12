from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from posts import views as posts_views
from users import views as user_views

urlpatterns = [
    # posts views
    path("", include(("posts.urls", "posts"), namespace="posts")),
    # user views
    path('users/', include(('users.urls', 'users'), namespace='users'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
