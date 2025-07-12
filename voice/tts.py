import pyttsx3
import threading

engine = pyttsx3.init()

def speak(text):
    def _speak():
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=_speak).start()
