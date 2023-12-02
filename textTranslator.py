from googletrans import Translator, LANGCODES, LANGUAGES

class TextTranslator(Translator):
    def trans(self, inputText: str, transLang: str) -> str:
        '''Translates text in the give translated language code 
        Look code by this URL "https://developers.google.com/admin-sdk/directory/v1/languages"'''
        print(len(LANGUAGES.values()))
        print(len(LANGCODES.values()))
        # Translator
        if not inputText:
            raise ValueError ("Input text must be a string and should be passed")
        if not transLang:
            raise ValueError("TransLang code must be a string and should be passed")
        
        translatedText = self.translate(text=inputText, dest=transLang)
        # Translated text in the given to translated language
        return translatedText