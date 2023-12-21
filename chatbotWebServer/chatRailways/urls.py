from django.urls import path
from . import views

# urlpatterns that define the URls and their function
urlpatterns = [
    path('', views.start_chat),
    path('text_translate/', views.translate, name='text_translate')
]