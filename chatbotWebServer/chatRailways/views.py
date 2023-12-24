from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chatRailways.chatbotModule.chatbot import Bot
import json


# Create your views here.
def renderWebPage(request):
    """
    The function `renderWebPage` returns a rendered web page using the template `chatbotUI.html`.
    
    :param request: The request parameter is an object that represents the HTTP request made by the
    client. It contains information such as the HTTP method (GET, POST, etc.), headers, and any data
    sent with the request
    :return: the rendered web page with the template 'chatbotUI.html'.
    """
    return render(request, 'chatbotUI.html')

# Railways chatbot Object
myRailwaysChatBot = Bot(r'chatRailways\chatbotModule\data\indianRailwaysData.csv')

def startChat(request):
    """
    The function `startChat` takes a user query as input, passes it to a chatbot, and returns the
    response of the chatbot as a JSON object.
    
    :param request: The `request` parameter is an object that represents the HTTP request made by the
    client. It contains information such as the request method (GET, POST, etc.), headers, and body
    :return: a JSON response containing the response of the chatbot.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        query = data.get('userQuery')
        print(query)
        responseOfTheRequest = myRailwaysChatBot.chat(query)
        print(responseOfTheRequest)
        result = {'response': responseOfTheRequest}
        return JsonResponse(result)
    