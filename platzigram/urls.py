from django.contrib import admin
from django.urls import path
from platzigram import views as local_views
from posts import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world',local_views.hello_world),
    path('hi', local_views.hi),
    path('challenge-number', local_views.challenge_numbers),
    path('say-hi/<str:name>/<int:age>/',local_views.say_hi),
    # posts views
    path('posts/',posts_views.list_posts),
]
