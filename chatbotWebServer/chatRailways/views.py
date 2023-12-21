from django.shortcuts import render
from django.http import HttpResponse
from chatbotModule.chatbot import Bot

# Create your views here.
def start_chat(request):
    # Render the HTML template
    # Take input query
    query = request.POST.get("query")
    myRailwaysChatBot = Bot(r'chatbotModule\data\indianRailwaysData.csv')
    response = myRailwaysChatBot.chat(query)
    return render(request, 'chatbotUI.html', {'response': response})