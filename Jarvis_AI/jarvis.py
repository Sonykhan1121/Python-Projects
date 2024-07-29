import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pyaudio
import sys
import AppOpener

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError as e:

            print("Not Understanding")
            return ""

def text_to_speech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    # 0 - male voice 1 - female voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)

    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    now = speech_to_text().lower()
    if now == 'hello':
        text_to_speech("Hello sir,I am DJ. what can i do for you?")
    elif now=='time':
        time = datetime.datetime.now().strftime("%I%M%p")
        text_to_speech(time)
    elif now == 'youtube':
        webbrowser.open('https://www.youtube.com/')
    elif now == 'hi':
        AppOpener.open("vscode")
    else:
        text_to_speech("Tell me hello")