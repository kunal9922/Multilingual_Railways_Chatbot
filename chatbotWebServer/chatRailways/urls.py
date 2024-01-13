from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns that define the URls and their function
urlpatterns = [
    path('', views.renderWebPage),
    path('chatbot/', views.startChat, name='startChat'),
    path('speech/', views.receive_audio, name='receiveAudio'),
]
# Add this line at the end of your urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)