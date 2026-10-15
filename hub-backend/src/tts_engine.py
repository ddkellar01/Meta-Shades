import pyttsx3

class TTSEngine:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 165)
        self.engine.setProperty('volume', 0.9)

    def speak(self, text: str):
        print(f"🔊 [Audio Output]: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
