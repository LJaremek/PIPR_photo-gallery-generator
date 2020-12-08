from googletrans import Translator

def translate(language_from = "pl", language_to = "en", text = "Witaj Świecie!"):
    translator = Translator(service_urls=['translate.googleapis.com'])
    new_test = translator.translate(text, dest = language_to, src = language_from)
    return new_test.text

# print(translate("pl", "en", "lubię stare buty"))
# print(translate())

