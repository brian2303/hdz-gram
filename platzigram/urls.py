from django.contrib import admin
from django.urls import path
from platzigram.views import hello_world,hi, challenge_numbers, say_hi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world', hello_world),
    path('hi', hi),
    path('challenge-number', challenge_numbers),
    path('say-hi/<str:name>/<int:age>/',say_hi)
]
