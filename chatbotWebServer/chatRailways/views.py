from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chatRailways.chatbotModule.chatbot import Bot
from chatRailways.chatbotModule.textTranslator import TextTranslator
import json
from chatRailways.chatbotModule.transcriber import MessageTranscriber
from django.http import FileResponse
import speech_recognition as sr
from pydub import AudioSegment
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
myRailwaysChatBot = Bot()
# Translator chatbot Object
trans = TextTranslator()
msgTrans = MessageTranscriber()

@csrf_exempt
def receive_audio(request):
    """
    Handles incoming POST requests containing audio data for speech recognition.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        JsonResponse: A JSON response containing the recognized text and language code (if successful),
                      or an error message (if unsuccessful).
    """
    global text_result
    if request.method == 'POST':
        audio_data = request.FILES.get('audio')
        print(type(audio_data.chunks()))
        if audio_data is None:
            return JsonResponse({'success': False, 'error': 'No audio data received in the request.'})

        try:
            # Process the audio data (you can use it, save it, etc.)
            # For example, save the audio file to a directory
            with open(r'chatRailways\static\audio\voice_input.wav', 'wb+') as destination:
                for chunk in audio_data.chunks():
                    destination.write(chunk)
                    
            lang = request.POST.get('lang')  # Retrieve 'lang' parameter from POST data
            # for hindi language speech recognition 
            if lang=="hi":
                sound = AudioSegment.from_file(r"chatRailways\static\audio\voice_input.wav")
                sound.export(r"chatRailways\static\audio\voice_input.wav", format="wav")
                try:
                    r = sr.Recognizer()
                    with sr.AudioFile(r"chatRailways\static\audio\voice_input.wav") as source:
                        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
                        audio = r.record(source)
                    # Use Google speech recognition for Hindi (hi-IN)
                    text_result = r.recognize_google(audio, language="hi-IN")
                except Exception as e:
                    print(e)
            else:
                text_result, lang = msgTrans.voice_to_text(r'chatRailways\static\audio\voice_input.wav')
            return JsonResponse({'success': True, 'text': text_result, 'langCode': lang})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})

def startChat(request):
    global result, langCode
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
        langCode = data.get('selectedLanguage')
        print(query, langCode)
        # Converting userQuery into English for the model understandings purpose
        # Translation layer 
        transText = trans.translate(query, 'en')
        # print(transText.text)
        botResponse = myRailwaysChatBot.chat(transText.text)
        
        # Translation layer 
        transText = trans.translate(botResponse, langCode)
        
        print(botResponse)
        
        # Sends response back to the frontend web page
        result = {'response': transText.text}
        return JsonResponse(result)

@csrf_exempt
def get_chatbot_speech(request):
    """
    Handles incoming POST requests for generating speech from the chatbot's response.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        FileResponse: An audio file (in WAV format) containing the synthesized speech.
    """
    msgTrans.text_to_voice(result['response'], langCode)
    # Assuming 'path_to_audio_file' is the path to your audio file
    path_to_audio_file = r'chatRailways\static\audio\textToVoice.wav'
    
    # Return the audio file as a response
    return FileResponse(open(path_to_audio_file, 'rb'), content_type='audio/wav')