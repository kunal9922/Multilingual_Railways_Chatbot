from django.urls import path
from . import views

# urlpatterns that define the URls and their function
urlpatterns = [
    path('', views.renderWebPage),
    path('chatbot/', views.startChat, name='startChat')
]