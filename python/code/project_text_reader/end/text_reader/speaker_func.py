import pyttsx3


def create_speaker():
    return pyttsx3.init()


def say(engine: pyttsx3.Engine, text: str):
    engine.say(text)
    engine.runAndWait()


def get_voices(engine: pyttsx3.Engine):
    return engine.getProperty("voices")


def set_voice_id(engine: pyttsx3.Engine, voice_id):
    engine.setProperty('voice', voice_id)


def set_voice(engine: pyttsx3.Engine, voice):
    engine.setProperty('voice', voice.id)