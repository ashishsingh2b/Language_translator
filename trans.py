from googletrans import Translator

def translate_text(input_text, source_language, target_language):
    translator = Translator()
    translated_text = translator.translate(input_text, src=source_language, dest=target_language).text
    return translated_text
