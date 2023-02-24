from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import random
import whisper


metin1 = """ Donec rutrum congue leo eget malesuada. Curabitur arcu erat, accumsan id imperdiet et, 
porttitor at sem. Vivamus magna justo, lacinia eget consectetur sed, 
convallis at tellus. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem."""
metin2 = """Cras ultricies ligula sed magna dictum porta. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed porttitor lectus nibh.  """
metin3 = """ Nulla porttitor accumsan tincidunt. Sed porttitor lectus nibh. Quisque velit nisi, pretium ut lacinia in,
elementum id enim. Curabitur aliquet quam id dui posuere blandit. Quisque velit nisi, pretium ut lacinia in, elementum id enim."""

dizi = [metin1, metin2, metin3]


r = sr.Recognizer()


def record(ask=False):
    with sr.Microphone()as source:

        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("asistan : anlayamadım")
        except sr.RequestError:
            print("asistan : sistem çalışmıyor")
        return voice


def speak(string):
    tts = gTTS(text=string, lang="tr")
    file = "answer.mp3"
    tts.save(file)
    print(dizi[random.randint(0, 2)])
    playsound(file)
    os.remove(file)



# speak("konuşmaya başla")


# voice = record()


# if voice != '':
#     voice = voice.lower()
#     print(voice)



