from django.urls import path
from . import views

# urlpatterns that define the URls and their function
urlpatterns = [
    path('hello/', views.say_hello)
]