from googletrans import Translator, LANGCODES, LANGUAGES

class TextTranslator(Translator):
    def trans(self, inputText: str, transLang: str) -> str:
        '''Translates text in the give translation language code 
        Look code by this URL "https://developers.google.com/admin-sdk/directory/v1/languages"'''
        # print(LANGUAGES.values())
        # print(LANGCODES.values())
        # Translator
        if not inputText:
            raise ValueError ("Input text must be a string and should be passed")
        if not transLang:
            raise ValueError("TransLang code must be a string and should be passed")

        return self.translate(text=inputText, dest=transLang).text