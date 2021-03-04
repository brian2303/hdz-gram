from django.contrib import admin
from django.urls import path
from platzigram.views import hello_world,hi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world', hello_world),
    path('hi', hi)
]
