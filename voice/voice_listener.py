import speech_recognition as sr
from ui.screen_state import add_transcript
import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def listen_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening for command...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"🧠 Heard: {text}")
        add_transcript("User: " + text)
        return text.lower()
    except sr.UnknownValueError:
        print("❗ Didn't understand audio.")
        add_transcript("User: [Unclear]")
        return ""
    except sr.RequestError as e:
        print(f"❌ API error: {e}")
        add_transcript("User: [Speech API Error]")
        return ""
