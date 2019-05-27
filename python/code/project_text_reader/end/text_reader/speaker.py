import pyttsx3


class Speaker:
    def __init__(self, engine=pyttsx3.init()):
        self._engine = engine

    def say(self, text: str):
        self._engine.say(text)
        self._engine.runAndWait()

    @property
    def voices(self):
        return self._engine.getProperty("voices")

    def set_voice_id(self, voice_id):
        self._engine.setProperty('voice', voice_id)

    def set_voice(self, voice):
        self._engine.setProperty('voice', voice.id)
