# Importing necessary modules required
import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

recog = spr.Recognizer()

mc = spr.Microphone()

# '#capture voice'
with mc as source:
    print("speak 'hello' to initiate the Translation!")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    recog.adjust_for_ambient_noise(source, duration=1)
    audio = recog.listen(source)
    MyText = recog.recognize_google(audio)
    MyText = MyText.lower()

if "hello" in MyText:
    translator = Translator()
    from_lang = 'en'
    to_lang = 'hi'
    with mc as source:
        print('speak a sentence... ')
        recog.adjust_for_ambient_noise(source, duration=1)
        audio = recog.listen(source)
        getsentence = recog.recognize_google(audio)
        print(getsentence)

        try:
            print('Phase to be Translated:', getsentence)
            texttranslate = translator.translate(getsentence, src=from_lang, dest=to_lang)
            print(texttranslate.text)
            print(texttranslate.src, texttranslate.dest)
            text = texttranslate.text
            speak = gTTS(text=text, lang=to_lang, slow=False)
            speak.save('captured_voice.mp3')
            os.system('start captured_voice.mp3')
        except spr.UnknownValueError:
            print("unable to understand the input")
        except spr.RequestError as e:
            print("unable to provide Required output".format(e))
        except Exception as error:
            print("Exception caught on main Exception class {}".format(error))
else:
    print("Please say 'hello' to initialize the Google translator")