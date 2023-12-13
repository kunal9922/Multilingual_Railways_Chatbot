from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def start_chat(request):
    # Render the HTML template
    return render(request, 'chatbotUI.html')

