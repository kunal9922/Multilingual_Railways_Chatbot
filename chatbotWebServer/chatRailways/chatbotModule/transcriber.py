import whisper
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