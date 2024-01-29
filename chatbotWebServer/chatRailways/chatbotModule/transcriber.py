import whisper
from gtts import gTTS
# import pprint

class MessageTranscriber():
    '''The `MessageTranscriber` class provides a method `voice_to_text` that transcribes audio files into
        text using the Whisper ASR model.'''
    model = whisper.load_model('base')
    def voice_to_text(self, audioFile) -> str and str:
        """
        The function `voice_to_text` takes an audio file as input and uses a model to transcribe the
        audio into text. It returns the transcribed text and the language code of the audio.
        
        :param audioFile: The audioFile parameter is the file path or object representing the audio file
        that you want to transcribe. It can be in various formats such as WAV, MP3, or FLAC
        :return: two values: a string representing the transcribed text from the audio file, and a
        string representing the language of the transcribed text.
        """
        text = self.model.transcribe(audioFile)
        # pprint.pprint(text)
        return text['text'], text['language']
    
    def text_to_voice(self, text: str, langCode: str):
        """
        The function `text_to_voice` generates a voice from the given text for a specified language code
        and saves it as a WAV file.
        
        :param text: The text parameter is the input text that you want to convert into speech. It can
        be string
        :param langCode: The langCode parameter is a language code that specifies the language of the
        text you want to convert to voice. For example, "en" for English, "fr" for French, "es" for
        Spanish, etc
        """
        speech = gTTS(text=text, lang=langCode, slow=False, tld="com.au")
        speech.save(r"chatRailways\static\audio\textToVoice.wav")